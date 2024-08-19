from django.urls import path
from . import views


urlpatterns = [
  path('indexpc/', views.indexpc, name='indexpc'),
  path('index_supplypc',views.index_supplypc, name='index_supplypc'),
  path('add_supplypc/', views.create_supplypc, name='add_supplypc'),
  path('add_productpc/', views.create_productpc, name='add_productpc'),
  path('base/', views.base, name='base'),
  path('supply_chartpc/', views.supply_chartpc, name='supply_chartpc'),
 
  path('sidebar/', views.sidebar, name='sidebar'),
  path ('editpc/<int:id>/', views.editpc, name='editpc'),
 
  path('deletepc/<int:id>/', views.deletepc, name='deletepc'),
  path ('viewpc/<int:id>', views.viewpc, name='viewpc'),
  
  path('add_supply_for_productpc/<int:product_id>/', views.add_supply_for_productpc, name='add_supply_for_productpc'),
  
  
  
]


 