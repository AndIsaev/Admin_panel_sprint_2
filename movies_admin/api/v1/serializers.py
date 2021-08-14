from rest_framework import serializers
from rest_framework.fields import UUIDField

from movies.models import FilmWork


class MoviesSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, )
    directors = serializers.StringRelatedField(many=True, )
    writers = serializers.StringRelatedField(many=True, )
    genres = serializers.StringRelatedField(many=True, )

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
            'genres',
            'actors',
            'directors',
            'writers',
        )
