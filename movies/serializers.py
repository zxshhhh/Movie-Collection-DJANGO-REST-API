from rest_framework import serializers
from .models import Movie
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
    def validate_release_year(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Release year cannot be in the future.")
        if value < datetime.date(1970, 1, 1):
            raise serializers.ValidationError("Release year cannot be before 1970.")
        return value
