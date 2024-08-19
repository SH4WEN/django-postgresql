from django.contrib import admin
from .models import Supply,Product



class SupplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price' )
    list_filter = ['price']
    
admin.site.site_header = 'Supply Management System by sh4wen'

# Register your models here.
admin.site.register(Supply)
admin.site.register(Product)