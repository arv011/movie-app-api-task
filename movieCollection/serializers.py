from rest_framework import serializers,fields
from movieCollection.models import UserMovieCollection
from django.db import transaction
from movie.models import Movie,GENRE_CHOICES


class MovieSerializer(serializers.ModelSerializer):
    genres = fields.MultipleChoiceField(choices=GENRE_CHOICES,required=False)
    class Meta:
        model = Movie    
        fields = ('uuid','title','description','genres')


class MovieCollectionSerializer(serializers.ModelSerializer):
    '''get movie collections details'''
    movies = MovieSerializer(many=True,read_only=True)

    class Meta:
        model = UserMovieCollection
        fields = ('uuid','title','description','owner','movies','updated_by')
        extra_kwargs = {
            'owner': {'write_only': True},
            'updated_by': {'write_only': True},
        }
    
    def __init__(self, *args, **kwargs):
        super(MovieCollectionSerializer, self).__init__(*args, **kwargs)
        if self.fields and not self.context.get('uu', None):
            self.fields.pop("movies")
