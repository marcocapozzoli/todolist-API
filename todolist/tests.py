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
    
    def test_todolist_list_authorized(self):
        """Verifica requisição GET quando usuário está antenticado"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_todolist_list_un_authorized(self):
        """Verifica requisição GET quando usuário não está authenticado"""
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_todolist_create(self):
        """Verificar se o usuário logado consegue criar alguma tarefa e se ela atribuída a ele"""
        data = {'task':'Programar', 'date':'2021-08-30','check':'Y'}
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['username'], self.user.username)
        
    def test_todolist_detail(self):
        """Verifica requisição GET/{id} quando usuário está authenticado"""
        response = self.client.get(reverse('todolist-detail', kwargs={'pk':1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todolist_update(self):
        """Verifica se o usuário logado consegue atualizar uma tarefa que ele criou"""
        data = {'task':'Programar update', 'date':'2021-08-30','check':'Y'}
        response = self.client.put(reverse('todolist-detail', kwargs={'pk':1}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_todolist_update_random_user(self):
        """Verifica se algum usuário não consegue atualizar uma tarefa que ele não criou"""
        random_user = CustomUser.objects.create(username='Evoe.cc',email='evoecc@gmail.com',password='pythonDRF')
        self.client.force_authenticate(user=random_user)
        data = {'task':'Programar update', 'date':'2021-08-30','check':'Y'}
        response = self.client.put(reverse('todolist-detail', kwargs={'pk':1}), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)