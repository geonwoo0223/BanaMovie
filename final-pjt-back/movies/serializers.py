from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta :
        model = Genre
        fields = ('id', 'name')

class MovieSerializer(serializers.ModelSerializer):
    genre_sl = GenreSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = ('id','movie_no','title','genre_sl','status','admin_reg','rate','vote_count','release_date','adult','overview','poster_path')

