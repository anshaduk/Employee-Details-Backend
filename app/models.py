from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
        