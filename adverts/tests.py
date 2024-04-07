from django.contrib.auth.models import User
from .models import Adverts
from rest_framework import status
from rest_framework.test import APITestCase


class AdvertListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='kevin', password='pass')

    def test_can_list_ads(self):
        kevin = User.objects.get(username='kevin')
        Adverts.objects.create(owner=kevin, title='test')
        response = self.client.get('/adverts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_ad(self):
        self.client.login(username='kevin', password='pass')
        response = self.client.post('/adverts/', {'title': 'test'})
        count = Adverts.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_ad(self):
        response = self.client.post('/adverts/', {'title': 'test'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)