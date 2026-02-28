from rest_framework import serializers
from .models import Movie, Review
import datetime
from django.utils import timezone

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title must be at least 2 characters long.")
        return value
    def validate_release_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Release date cannot be in the future.")
        if value < datetime.date(1970, 1, 1):
            raise serializers.ValidationError("Release date cannot be before 1970.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    def validate_rating(self, value):
        if value < 1.0 or value > 5.0:
            raise serializers.ValidationError("Rating must be between 1.0 and 5.0.")
        return value