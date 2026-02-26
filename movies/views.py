from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Movie
from .serializers import MovieSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'director']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def popular(self, request, *args, **kwargs):
        movies = Movie.objects.order_by('-views')[:10]
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def trending(self, request, *args, **kwargs):
        last_week = timezone.now() - timedelta(days=7)
        movies = Movie.objects.filter(
            created_at__gte=last_week
        ).order_by('-views')[:10]
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def latest(self, request, *args, **kwargs):
        movies = Movie.objects.order_by('-release_date')[:10]
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)