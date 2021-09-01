from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from users.models import CustomUser


class CreateUserTestCase(APITestCase):

    def test_registration(self):
        """Verifica se um usuário consegue se registrar no sistema"""
        data = {'username': 'evoe',
                'email':'evoe@localhost.com',
                'password1': 'pythonDRF',
                'password2': 'pythonDRF'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
