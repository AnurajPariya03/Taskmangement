from django.contrib import admin
from .models import Task, UserCredentials, CustomUser

admin.site.register(Task)
admin.site.register(UserCredentials)
admin.site.register(CustomUser)