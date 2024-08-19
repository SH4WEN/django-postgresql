from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Production', 'Production User'),
        ('Warehouse', 'Warehouse User'),
        ('Admin', 'Production Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='production')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='personel_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='personel_user_permissions',
        blank=True,
    )    