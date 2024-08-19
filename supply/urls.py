from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('index_supply',views.index_supply, name='index_supply'),
  path('add_supply/', views.create_supply, name='add_supply'),
  path('add_product/', views.create_product, name='add_product'),
  path('base/', views.base, name='base'),
  path('supply_chart/', views.supply_chart, name='supply_chart'),
 
  path('sidebar/', views.sidebar, name='sidebar'),
  path ('edit/<int:id>/', views.edit, name='edit'),
 
  path('delete/<int:id>/', views.delete, name='delete'),
  path ('view/<int:id>', views.view, name='view'),
  
  path('add_supply_for_product/<int:product_id>/', views.add_supply_for_product, name='add_supply_for_product'),
  
  
  
]


 