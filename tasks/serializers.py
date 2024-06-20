from rest_framework import serializers
from .models import Task, UserCredentials, CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class UserCredentialsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserCredentials
        fields = ['id', 'user', 'username', 'password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'completed', 'created_at']
