import requests

from django.shortcuts import get_object_or_404
from django.core import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer
from .models import Movie, Genre


@api_view(['GET'])
def getMovies(request):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=e8067ff017c9f1acd66ea2924205aae6'
    payload = {
        'language' : 'ko'
    }
    r = requests.get(url, params=payload)
    movies = r.json()
    # original_data = Movie.objects.all().filter
    for movie in movies['results']:
        # 존재하는 영화는 다시 pass
        if Movie.objects.all().filter(movie_no=movie['id']).exists():
            continue
        movie_new = Movie(
            movie_no= movie['id'],
            title= movie['title'],
            release_date= movie['release_date'],
            poster_path= movie['poster_path'],
            adult= movie['adult'],
            overview= movie['overview'],
        )
        movie_new.save()

        for genre in movie['genre_ids']:
            movie_new.genres.add(genre)
    completed_movies = Movie.objects.all()
    serialzed_movies = MovieSerializer(completed_movies, many=True)
    
    return Response(serialzed_movies.data)
    

