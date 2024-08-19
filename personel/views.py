from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User





from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .forms import RegistrationForm


# import uuid
# Create your views here.


  

def login (request):
    
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid input')
    return render(request,'personel/login.html')


def logout(request):
    auth_logout(request)
    
    return redirect('login')


# token base
# def login(request):
#     if request.method == 'POST':
#         if 'username' in request.POST and 'password' in request.POST:
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth_login(request, user)
#                 # Generate a unique token for the user session
#                 token = uuid.uuid4().hex
#                 request.session['token'] = token
#                 return redirect('index')
#             else:
#                 messages.error(request, 'Invalid input')
#     return render(request, 'personel/login.html')

# def logout(request):
#     auth_logout(request)
#     # Invalidate the token
#     request.session.pop('token', None)
#     return redirect('login')




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            role = form.cleaned_data['role']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.error(request, 'Passwords do not match')
            else:
                otp = get_random_string(length=6, allowed_chars='0123456789')
                user = User.objects.create_user(username=username, email=email, password=password)
                user.role = role
                user.is_active = False
                user.save()
                send_mail(
                    'Verify your email',
                    f'Your OTP is {otp}',
                    'your_email@example.com',
                    [email],
                    fail_silently=False,
                )
                request.session['otp'] = otp
                request.session['username'] = username
                return redirect('verify_otp')
    else:
        form = RegistrationForm()
    return render(request, 'personel/register.html', {'form': form})

def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == request.session['otp']:
            user = User.objects.get(username=request.session['username'])
            user.is_active = True
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'Invalid OTP')
    return render(request, 'personel/verify-otp.html')

def reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            otp = get_random_string(length=6, allowed_chars='0123456789')
            user = User.objects.get(email=email)
            send_mail(
                'Reset password',
                f'Your OTP is {otp}',
                'your_email@example.com',
                [email],
                fail_silently=False,
            )
            request.session['otp'] = otp
            request.session['email'] = email
            return redirect('verify_otp_reset')
        else:
            messages.error(request, 'Email not found')
    return render(request, 'personel/reset-password.html')

def verify_otp_reset(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        if otp == request.session['otp']:
            email = request.session['email']
            user = User.objects.get(email=email)
            return redirect('set_password', user_id=user.id)
        else:
            messages.error(request, 'Invalid OTP')
    return render(request, 'personel/verify-otp-reset.html')

def set_password(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        password = request.POST['password']
        user.set_password(password)
        user.save()
        messages.success(request, 'Password reset successfully')
        return redirect('login')
    return render(request, 'personel/set-password.html', {'user_id': user_id})