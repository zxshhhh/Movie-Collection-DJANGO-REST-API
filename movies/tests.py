from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Movie

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "/api/v1/movies/"
        self.movie_data = {
            "title": "Inception",
            "description": "A mind-bending thriller.",
            "director": "Christopher Nolan",
            "release_date": "2010-07-16",
            "rating": 5.0,
            "genre": "SCI_FI"
        }

    def test_create_movie(self):
        response = self.client.post(self.url, self.movie_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 1)
