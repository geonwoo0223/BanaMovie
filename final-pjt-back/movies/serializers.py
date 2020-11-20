from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title','release_date','adult','overview','poster_path')

