from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie

class MovieAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/movies/'
        self.movie_data = {
            "title": "Inception",
            "director": "Christopher Nolan",
            "release_year": 2010,
            "rating": 8.8
        }

    def test_create_movie(self):
        response = self.client.post(self.url, self.movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Movie.objects.get().title, "Inception")
