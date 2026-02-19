from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=150)
    release_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1888),  # first film
            MaxValueValidator(date.today().year)
        ]
    )
    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0)
        ]
    )

    def __str__(self):
        return f"{self.title} ({self.release_year})"
