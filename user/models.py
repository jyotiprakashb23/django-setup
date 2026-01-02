from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.phone_number
    
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True,null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"