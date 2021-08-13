from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from rest_framework import mixins, viewsets
from .serializers import MoviesSerializer
from movies.models import FilmWork


class MoviesAPIView(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = FilmWork.objects.all()
    serializer_class = MoviesSerializer
