import requests

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre, UserGenre


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

@api_view(['GET'])
def getGenre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommendMovie(request):
    # 로그인 되어있는 유저
    login_user = request.user

    # 해당 유저가 어떤 장르의 영화를 좋아했는지
    genre_status = get_object_or_404(UserGenre, user_id=login_user.id)
    
    best = max(genre_status, key=lambda x: genre_status.genre_count)
    
    # 모든 영화를 받아온다
    movies = Movie.objects.all()

    # 그 중 해당 장르를 포함한 영화만

    recommended = Movie.movie_genres.all().filter(genre_id=best.genre_id)
    serialzed_movies = MovieSerializer(recommended, many=True)
    
    return Response(serialzed_movies.data)

@api_view(['POST'])
def addMovie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
