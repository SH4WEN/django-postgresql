from django.urls import path
from . import views


urlpatterns = [
  path('login', views.login, name='login'),
  path ('logout/', views.logout, name='logout'),
  path('register/', views.register, name='register'),
  path('reset/', views.reset, name='reset'),
  path('set_password/<int:user_id>//', views.set_password, name='set_password'),
  path('verify_otp/', views.verify_otp, name='verify_otp'),
  path('verify_otp_reset/', views.verify_otp_reset, name='verify_otp_reset'),
  
]
