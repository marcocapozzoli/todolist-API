from rest_framework import status, viewsets
from rest_framework.response import Response
from users.models import CustomUser

from .models import ToDoList
from .serializers import CustomUserSerializer, ToDoListSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        users = CustomUser.objects.all()
        return users

class ToDoListViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        todolist = ToDoList.objects.all()
        return todolist