from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import CustomUser

from .models import ToDoList


class ToDoListTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('todolist-list')
        self.user = CustomUser.objects.create(username='Evoe',email='evoe@gmail.com',password='pythonDRF')
        self.todolist = ToDoList.objects.create(task = 'Programar', date = '2021-08-30', check = 'N', user = self.user)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)