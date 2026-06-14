from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('manager','Manager'),
        ('employee','Employee'),
    )

    role = models.CharField( max_length=20, choices=ROLE_CHOICES, default = 'employee')

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank = True) 




