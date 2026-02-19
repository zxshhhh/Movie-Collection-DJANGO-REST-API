from rest_framework import serializers
from .models import Movie
from datetime import date

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title must be at least 2 characters long.")
        return value

    def validate_release_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Release year cannot be in the future.")
        return value
