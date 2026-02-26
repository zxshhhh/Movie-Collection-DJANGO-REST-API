from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime
    
class Movie(models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = 'ACTION', 'Action'
        COMEDY = 'COMEDY', 'Comedy'
        DRAMA = 'DRAMA', 'Drama'
        HORROR = 'HORROR', 'Horror'
        SCI_FI = 'SCI_FI', 'Sci-Fi'
        ROMANCE = 'ROMANCE', 'Romance'
        FANTASY = 'FANTASY', 'Fantasy'
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
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.release_date.year})"