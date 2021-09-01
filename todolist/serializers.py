from rest_framework import serializers
from users.models import CustomUser

from .models import ToDoList


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
    
class ToDoListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = ToDoList
        fields = ['id', 'task', 'date', 'check', 'user']