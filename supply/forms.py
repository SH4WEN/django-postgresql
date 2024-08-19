from django import forms
from .models import Product, Supply

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product','unit', 'description', 'branch')
        labels = {
            'product': 'Product Name',
            'unit': 'Unit',
            'description': 'Product Description',
            'branch': 'Branch'
        }
        widgets = {
            
            'product': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'unit': forms.Select(attrs={'class': 'form-control form-control-sm'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'branch': forms.Select(attrs={'class': 'form-control form-control-sm'}), 
        }

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ('quantity',  'price', 'product_date')
        labels = {
            # 'product': 'Product Name',                           
            'quantity': 'Product Quantity',
           
            'price': 'Product Price',
            'product_date': 'Product Date',
        }
        widgets = {
            # 'product': forms.Select(attrs={'class': 'form-control form-control-sm'}),           
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
                        
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'product_date': forms.DateTimeInput(attrs={'class': 'form-control form-control-sm'}),
        }






# from django import forms
# from .models import Supply

# class SupplyForm(forms.ModelForm):
#     class Meta:
#         model = Supply
#         fields = ['product_date', 'quantity', 'unit', 'product_name', 'product_description', 'price']
#         labels = {
#             'product_date': 'Product Date',
#             'quantity': 'Product Quantity',
#             'unit': 'Unit',
#             'product_name': 'Product Name',
#             'product_description': 'Product Description',
#             'price': 'Product Price'
#         }
#         widgets = {
#             'product_date': forms.DateTimeInput(attrs={'class': 'form-control form-control-sm'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
#             'unit': forms.Select(attrs={'class': 'form-control form-control-sm'}),
#             'product_name': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
#             'product_description': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
#         }




