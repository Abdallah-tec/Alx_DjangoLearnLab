from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"



    
class CustomUserManager(BaseUserManager):
    def create_user(self,username : str,email : str|None = ... , password : str | None = ...,**extra_fields: any) -> any:
        return super().create_user(username,email,password,**extra_fields)
    
    def create_superuser(self, username: str, email: str | None, password: str | None, **extra_fields: Any) -> Any:
        return super().create_superuser(username, email, password, **extra_fields)
        
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=true)
    profile_photo = models.ImageField(upload_to='profile_pics/')
    objects = CustomUserManager()

    def __str__(self):
        return self.username