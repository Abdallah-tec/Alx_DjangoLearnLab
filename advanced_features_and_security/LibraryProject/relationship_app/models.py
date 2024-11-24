from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self) -> str:
        return f"'{self.title}' by '{self.author}'"
class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book , related_name='library')

    def __str__(self) -> str:
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE,related_name="model")

    def __str__(self) -> str:
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class UserProfile(models.Model):
    class Role(models.TextChoices):
        admin = "Admin"
        librarian = "Librarian"
        member = "Member"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'userprofile')
    role = models.CharField(choices=Role, max_length=10, default=Role.member)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s profile. Role: {self.role}"