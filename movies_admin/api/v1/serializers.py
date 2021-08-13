from rest_framework import serializers
from movies.models import FilmWork


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmWork
        fields = (
            'id',
            'title',
            'description',
            'creation_date',
            'certificate',
            'rating',
            'type',
            'persons',
            'genres',
        )
