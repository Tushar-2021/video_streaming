from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Video

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-create')
        data = {'username': 'testuser', 'password': 'testpass', 'email': 'test@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class VideoTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_video(self):
        url = reverse('video-list-create')
        data = {'name': 'Test Video', 'url': 'http://example.com/video.mp4'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
