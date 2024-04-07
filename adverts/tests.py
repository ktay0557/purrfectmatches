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


class AdvertDetailViewTests(APITestCase):
    def setUp(self):
        kevin = User.objects.create_user(username='kevin', password='pass')
        levin = User.objects.create_user(username='levin', password='pass')
        Adverts.objects.create(
            owner=kevin, title='test', content='kevins content'
        )
        Adverts.objects.create(
            owner=levin, title='test 2', content='levins content'
        )

    def test_can_retrieve_ad_using_valid_id(self):
        response = self.client.get('/adverts/1/')
        self.assertEqual(response.data['title'], 'test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_ad_using_invalid_id(self):
        response = self.client.get('/adverts/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_ad(self):
        self.client.login(username='kevin', password='pass')
        response = self.client.put('/adverts/1/', {'title': 'tested'})
        advert = Adverts.objects.filter(pk=1).first()
        self.assertEqual(advert.title, 'tested')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_user_ad(self):
        self.client.login(username='kevin', password='pass')
        response = self.client.put('/adverts/2/', {'title': 'tested'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
