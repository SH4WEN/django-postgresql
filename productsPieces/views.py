from django.shortcuts import render, redirect
from .forms import ProductForm
from .forms import SupplyForm
import json
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Productpc, Supplypc
from django.db.models import Sum
from django.core import serializers
from django.contrib import messages

# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             new_name = form.cleaned_data['name']
#             new_description = form.cleaned_data['description']
#             new_branch = form.cleaned_data['branch']
            
#             new_product = Product(
#                name = new_name,
#                description = new_description,
#                branch = new_branch,
              
#             )
#             new_product.save()
            
#             products = Product.objects.all()  # Get all products
#             return render(request, 'supply/add_product.html', {
#                 'form': ProductForm(),
#                 'products': products,  # Pass products to the template
#                 'success': True
#             })
                      
#     else:
#         products = Product.objects.all()  # Get all products
#         form = ProductForm()
#     return render(request, 'supply/add_product.html', {
#         'form': form,
#         'products': products  # Pass products to the template
#     })

# def create_supply(request):
#     if request.method == 'POST':
#         form = SupplyForm(request.POST)
#         if form.is_valid():
#             new_product_date = form.cleaned_data['product_date']
#             new_product_quantity = form.cleaned_data['quantity']
#             new_unit = form.cleaned_data['unit']
#             new_product = form.cleaned_data['product']
#             new_price = form.cleaned_data['price']
            
#             new_supply = Supply(
#                product_date = new_product_date,
#                quantity = new_product_quantity,
#                unit = new_unit,
#                product = new_product,
#                price = new_price
#             )
#             new_supply.save()
            
#             return render(request, 'supply/add_supply.html', {
#                 'form': SupplyForm(),
#                 'success': True
#             })
                      
#     else:
#         form = SupplyForm()
#     return render(request, 'supply/add_supply.html', {
#         'form': form
#     })



# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             new_product = form.cleaned_data['product']
#             new_unit = form.cleaned_data['unit']
#             new_description = form.cleaned_data['description']
#             new_branch = form.cleaned_data['branch']
            
#             new_product = Product(
#                product = new_product,
#                unit = new_unit,
#                description = new_description,
#                branch = new_branch,
#             )
#             new_product.save()
            
#             return redirect('index')  # Redirect to index.html
                      
#     else:
#         products = Product.objects.all()  # Get all products
#         form = ProductForm()
#     return render(request, 'supply/add_product.html', {
#         'form': form,
#         'products': products  # Pass products to the template
#     })

def create_productpc(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be Login")
        return redirect('login')  # Redirect to login page if user is not authenticated
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = form.cleaned_data['product']
            if Productpc.objects.filter(product=new_product).exists():
                messages.error(request, "Product already exists")
                return redirect('add_productpc')  # Redirect back to the create product page
            else:
                new_unit = form.cleaned_data['unit']
                new_description = form.cleaned_data['description']
                new_branch = form.cleaned_data['branch']
                
                new_product = Productpc(
                   product = new_product,
                   unit = new_unit,
                   description = new_description,
                   branch = new_branch,
                )
                new_product.save()
                
                return redirect('indexpc')  # Redirect to index.html
                      
    else:
        products = Productpc.objects.all()  # Get all products
        form = ProductForm()
    return render(request, 'pieces/add_productpc.html', {
        'form': form,
        'products': products  # Pass products to the template
    })








def create_supplypc(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be Login")
        return redirect('login')  # Redirect to login page if user is not authenticated
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            new_product_date = form.cleaned_data['product_date']
            new_product_quantity = form.cleaned_data['quantity']  
            new_product = form.cleaned_data['product']
            new_price = form.cleaned_data['price']
            
            new_supply = Supplypc(
               product_date = new_product_date,
               quantity = new_product_quantity,
               product = new_product,
               price = new_price
            )
            new_supply.save()
            
            return redirect('indexpc')  # Redirect to index.html
                      
    else:
        form = SupplyForm()
    return render(request, 'pieces/add_supplypc.html', {
        'form': form
    })

def add_supply_for_productpc(request, product_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be Login")
        return redirect('login')  # Redirect to login page if user is not authenticated
    product = Productpc.objects.get(id=product_id)
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            new_product_date = form.cleaned_data['product_date']
            new_product_quantity = form.cleaned_data['quantity']        
            new_price = form.cleaned_data['price']
            
            new_supply = Supplypc(
               product_date = new_product_date,
               quantity = new_product_quantity,
               product = product,
               price = new_price
            )
            new_supply.save()
            
            return redirect('indexpc')  # Redirect to index.html
                      
    else:
        form = SupplyForm()
        
    return render(request, 'pieces/add_supplypc.html', {
        'form': form,
        'product': product,
        
    })











# def index(request):
#     products = Product.objects.all()
    
#     return render(request, 'supply/index.html', {'products': products})
   


# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')[:5]
#     for person in queryset:
#         labels.append(person.product.name)  
#         data.append(person.price)
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': Product.objects.all()
#     }
    
#     return render(request, 'supply/index.html', context)


# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')[:5]
#     for person in queryset:
#         labels.append(person.product.name)  
#         data.append(person.price)
    
#     products = Product.objects.all()
#     total_quantities = {}
#     for product in products:
#         total_quantities[product.name] = Supply.objects.filter(product=product).aggregate(Sum('quantity'))['quantity__sum'] or 0
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'total_quantities': total_quantities  # Pass total quantities to the template
#     }
    
#     return render(request, 'supply/index.html', context)









# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')
#     for person in queryset:
#         labels.append(person.product.product)
#         data.append(person.price)
    
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#     }
    
#     return render(request, 'supply/index.html', context)
# 


# final index
# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')
#     for person in queryset:
#         labels.append(person.product.product)
#         data.append(person.price)
    
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     # Calculate total quantity for all products
#     total_quantity = Supply.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'total_quantity': total_quantity,
#     }
    
#     return render(request, 'supply/index.html', context)



# final
# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('quantity')
#     for person in queryset:
#         labels.append(person.product.product)
#         data.append(person.product.supply_set.aggregate(total_quantity=Sum('quantity'))['total_quantity'])
    
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     # Calculate total quantity for all products
#     total_quantity = Supply.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'total_quantity': total_quantity,
#     }
    
#     return render(request, 'supply/index.html', context)


# def index(request):
#     labels = []
#     data = []
    
#     # Group products by category (Product instances)
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     # Create lists for labels and data
#     for product in products:
#         labels.append(product.product)
#         data.append(product.total_quantity)
    
#     # Calculate total quantity for all products
#     total_quantity = Supply.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
#     context = {
#         'labels': json.dumps(labels),
#         'products': products,
#         'data': json.dumps(data),
#         'total_quantity': total_quantity,
#     }
    
#     return render(request, 'supply/index.html', context)


# semi
# def index(request):
#     labels = []
#     data = []
#     # Group products by category (Product instances)
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     # Group products by name
#     supply = Supply.objects.values('product__product').annotate(total_quantity=Sum('quantity'))
    
#     # Create lists for labels and data
#     for supply in products:
#         labels.append(supply['product__product'])
#         data.append(supply['total_quantity'])
    
#     # Calculate total quantity for all products
#     total_quantity = Supply.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'total_quantity': total_quantity,
#     }
    
#     return render(request, 'supply/index.html', context)


def indexpc(request):
    labels = []
    data = []
    # Group products by category (Product instances)
    products = Productpc.objects.annotate(total_quantity=Sum('supplypc__quantity'))
    
    # Create lists for labels and data
    for product in products:
        labels.append(product.product)
        data.append(product.total_quantity)
    
    # Calculate total quantity for all products
    total_quantity = Supplypc.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
        'products': products,
        'total_quantity': total_quantity,
    }
    
    return render(request, 'pieces/indexpc.html', context)




# def index(request):
#     labels = []
#     data = []
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     for product in products:
#         labels.append(product.product)
#         data.append(product.total_quantity)
    
#     total_quantity = Supply.objects.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'total_quantity': total_quantity,
#     }
    
#     return render(request, 'supply/index.html', context)




# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')
#     for person in queryset:
#         labels.append(person.product.product)
#         data.append(person.price)
    
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
    
#     # Calculate total quantity for each unit type
#     total_quantities = {}
#     for supply in Supply.objects.all():
#         if supply.unit not in total_quantities:
#             total_quantities[supply.unit] = 0
#         total_quantities[supply.unit] += supply.quantity
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'total_quantities': total_quantities,
#     }
    
#     return render(request, 'supply/index.html', context)



# def index(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')
#     for person in queryset:
#         labels.append(person.product)  
#         data.append(person.price)
    
#     products = Product.objects.annotate(total_quantity=Sum('supply__quantity'))
#     products_json = serializers.serialize('json', products)
    
#     context = {
#         'labels': json.dumps(labels),
#         'data': json.dumps(data),
#         'products': products,
#         'products_json': products_json,
#     }
    
#     return render(request, 'supply/index.html', context)







def base (request):
 return render (request, 'base.html')


# def supply_chart(request):
#     labels = []
#     data = []
    
#     queryset = Supply.objects.order_by('price')
#     for person in queryset:
#         labels.append(person.products.product)  # Replace 'product.name' with the correct attribute
#         data.append(person.price)
#     return render(request, 'dashboard/supply_chart.html', {
#         'labels': json.dumps(labels),
#         'data' : json.dumps(data)
#     })
    
def supply_chartpc(request):
    # if not request.user.is_authenticated:
    #     messages.error(request, "You must be Login")
    #     return redirect('login')  # Redirect to login page if user is not authenticated
    labels = []
    data = []
    
    queryset = Supplypc.objects.order_by('price')
    for person in queryset:
        labels.append(person.product.product)
        data.append(person.price)
    return render(request, 'dashboard/supply_chartpc.html',{
        'labels': json.dumps(labels),
        'data' : json.dumps(data)
    })
    
    
    
    
    
    
    
def sidebar(request):
    return render (request, 'partials/sidebar.html')



# def edit (request, id):
#     if request.method=='POST':
#         product = Product.objects.get(pk=id)
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect (request,'supply/edit.html', {
#                 'form': form,
#                 'success': True
#             })
#     else:
#         supply = Product.objects.get(pk=id)
#         form = ProductForm(instance=supply)
#     return render(request, 'supply/edit.html', {
#         'form': form
#     })
    
    
    
def editpc(request, id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be Login")
        return redirect('login')  # Redirect to login page if user is not authenticated
    if request.method == 'POST':
        product = Productpc.objects.get(pk=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('indexpc')  # Redirect to the index view
    else:
        supply = Productpc.objects.get(pk=id)
        form = ProductForm(instance=supply)
    return render(request, 'pieces/editpc.html', {
        'form': form
    })
    
    
    
    
    
def deletepc (request, id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be Login")
        return redirect('login')  # Redirect to login page if user is not authenticated
    if request.method == 'POST':
        product= Productpc.objects.get(pk=id)
        product.delete()
    return HttpResponseRedirect(reverse('indexpc'))
        






        
def viewpc (request):
    products = Productpc.objects.all()
    return render(request, 'pieces/indexpc.html', {'products': products})














# suply def

def index_supplypc (request):
    return render (request, 'pieces/index_supplypc.html', {
        'supply': Supplypc.objects.all()
    })
    
# def  view_supply (request, id):
#     supply= Supply.objects.get(pk=id)
#     return HttpResponseRedirect(reverse('index')) 

# def add(request):
#     if request.method == 'POST':
#         form = SupplyForm(request.POST)
#         if form.is_valid():
#             new_product_date = form.cleaned_data['product_date']
#             new_product_quantity = form.cleaned_data['quantity']
#             new_unit = form.cleaned_data['unit']
#             new_product_name = form.cleaned_data['product_name']
#             new_product_description = form.cleaned_data['product_description']
#             new_price = form.cleaned_data['price']
            
#             new_supply = Supply(
#                product_date = new_product_date,
#                quantity = new_product_quantity,
#                unit = new_unit,
#                product_name = new_product_name,
#                product_description = new_product_description,
#                price = new_price
#             )
#             new_supply.save()
#             return render(request, 'supply/add.html', {
#                 'form': SupplyForm(),
#                 'success': True
#             })
#     else:
#         form = SupplyForm()
#     return render(request, 'supply/add.html', {
#         'form': form
#     })
    
    
    
# def edit (request, id):
#     if request.method=='POST':
#         supply = Supply.objects.get(pk=id)
#         form = SupplyForm(request.POST, instance=supply)
#         if form.is_valid():
#             form.save()
#             return render (request,'supply/edit.html', {
#                 'form': form,
#                 'success': True
#             })
#     else:
#         supply = Supply.objects.get(pk=id)
#         form = SupplyForm(instance=supply)
#     return render(request, 'supply/edit.html', {
#         'form': form
#     })

# def delete(request, id):
#     if request.method == 'POST':
#         supply = Supply.objects.get(pk=id)
#         supply.delete()
#     return HttpResponseRedirect(reverse('index'))
        