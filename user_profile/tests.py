from django.test import TestCase
from users.models import Users
from rest_framework import status
from user_profile.models import User_profile
from rest_framework.test import APITestCase, APIClient
from django.core.files import File
import mock
import json

class TestUserProfile(TestCase):
    def setUp(self):
        user_inst = Users.objects.create(id=1, username='root')
    def test_view(self):
        user_get = Users.objects.get(id=1,username='root')
        self.client.force_login(user_get)
        res = self.client.get('/profile/')
        self.assertEqual(res.status_code,200)

    def test_update_image(self):
        image_create = User_profile.objects.create(id=1,avatar='*.png')
        image_update = User_profile.objects.update(avatar='*.jpg')
        res = self.client.post(f'/profile/update_avatar/{image_create.id}/')
        self.assertEqual(res.status_code,302)
    
    def test_update_name(self):
        user_get = Users.objects.get(id=1)
        name_update = Users.objects.update(id=1,username='lop')
        res=self.client.post(f'/users/update_username/{user_get.id}/')
        self.assertEqual(res.status_code,200)

class TestUserApi(APITestCase,APIClient):
    def test_view_api_profile(self):
        res = self.client.get('/profile/api/profile/')
        self.assertEqual(res.status_code,status.HTTP_200_OK)
