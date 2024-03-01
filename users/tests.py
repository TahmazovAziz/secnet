import json
from django.test import TestCase
from users.models import Users
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class UsersTest(TestCase):
    def setUp(self):
        user = Users.objects.create(username='root')
    def test_view(self):
        res = self.client.get('/users/userslogin/')
        self.assertEqual(res.status_code,200)
    def test_create(self):
        user_login = Users.objects.get(username='root')
        self.client.force_login(user_login)
        res = self.client.post('/users/userslogin/')
        self.assertEqual(res.status_code,200)

class  TestUserApi(APITestCase,APIClient):
    def setUp(self):
        self.user = Users.objects.create(username='root')
    
    def test_view_api_user(self):
        res = self.client.get('/users/api/users/')
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_create_api_user(self):
        user={
            "username":"ak74"
        }

        res = self.client.post('/users/api/users/',user,format='json')
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)