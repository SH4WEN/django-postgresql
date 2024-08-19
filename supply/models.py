from django.db import models
from datetime import datetime
from django.core.validators import ValidationError

# Create your models here.
# class Supply (models.Model):
    # product_id=models.PositiveBigIntegerField()
    # product_date = models.DateTimeField(default=datetime.today())
    # quantity = models.PositiveBigIntegerField()
    # unit = models.CharField(max_length=10, choices=[
    #     ('kg', 'Kilograms'),
    #     ('piece', 'Pieces'),
    # ])
    # product_name = models.CharField(max_length=200)
    # product_description = models.CharField(max_length=500)
    # price =models.FloatField()
     
# class Mete:
#     verbose_name_plural = 'Supply as of now'
    
    # def __str__(self):
    #     return f'Product: {self.product_name}'
    
    
class Product(models.Model):
  product  = models.CharField(max_length=200)
  
  unit = models.CharField(max_length=10, choices=[
      ('g', 'Grams'),
      ('kg', 'Kilograms'),
      ('ton', 'Tons'),
      
  ])
  description = models.CharField(max_length=500)
  branch = models.CharField(max_length=200, choices=[
      ('A', 'PRODUCTION A'),
      ('B', 'PRODUCTION B'),
      ('C', 'PRODUCTION C'),
  ])
  
 
  def __str__(self):
      return f'Product: {self.product}'
    
    
class Supply(models.Model):
  product = models.ForeignKey('Product', on_delete=models.CASCADE)
  product_date = models.DateTimeField(default=datetime.today())
  quantity = models.PositiveBigIntegerField()
  
  price = models.FloatField()

  def __str__(self):
      return f'Product: {self.product}'
  
    