from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add related_name to avoid clashes with built-in User model
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

    def __str__(self):
        return self.username 

class UserCredentials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='credentials')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    # You can add other fields like security questions, last login time, etc.

    def __str__(self):
        return self.user.username

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
