from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.db.models import Avg
import datetime

class Movie(models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = 'ACTION', 'Action'
        COMEDY = 'COMEDY', 'Comedy'
        DRAMA = 'DRAMA', 'Drama'
        HORROR = 'HORROR', 'Horror'
        SCI_FI = 'SCI_FI', 'Sci-Fi'
        ROMANCE = 'ROMANCE', 'Romance'
    title = models.CharField(max_length=200)
    description = models.TextField(default="No description available.")
    director = models.CharField(max_length=150)
    views = models.PositiveIntegerField(default=0)
    genre = models.CharField(
        max_length=20,
        choices=GenreChoices.choices
    )
    release_date = models.DateField(
        validators=[
            MinValueValidator(datetime.date(1970, 1, 1)),
            MaxValueValidator(timezone.now().date())
        ]
    )
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ],
        default=1.0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        return self.reviews.aggregate(
            avg_rating=Avg("rating")
        )["avg_rating"] or 0

    def review_count(self):
        return self.reviews.count()

    def __str__(self):
        return f"{self.title} ({self.release_date.year})"

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    reviewer_name = models.CharField(max_length=100)
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title}"