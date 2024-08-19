from django.contrib import admin
from .models import Supplypc,Productpc



class SupplyAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'price' )
    list_filter = ['price']
    
admin.site.site_header = 'Supply Management System by sh4wen'

# Register your models here.
admin.site.register(Supplypc)
admin.site.register(Productpc)