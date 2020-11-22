import requests

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, GenreSerializer, ReviewSerializer, ReviewUserSerializer
from .models import Movie, Genre, UserGenre, Review


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
    # print(request.data)
    movieInfo = request.data['movieInfo']
    genres = request.data['genreInfo']
    movie_new = Movie(
        movie_no= movieInfo['movie_no'],
        title= movieInfo['title'],
        release_date= movieInfo['release_date'],
        poster_path= movieInfo['poster_path'],
        adult= movieInfo['adult'],
        overview= movieInfo['overview'],
        status= movieInfo['status'],
        admin_reg= movieInfo['admin_reg']
    )
    movie_new.save()
    for genre in genres['genres']:
        movie_new.genres.add(genre)
    serializer = MovieSerializer(movie_new)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movieDetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET','POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_add_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        review = Review.objects.filter(movie_id=movie_pk, user_id=request.user.id)
        temp = list(review.values())
        new = temp[0]
        new['user'] = request.user
        new['movie'] = movie
        serializer = ReviewSerializer(new)



        return Response(serializer.data)
    else:
        review = request.data
        review_new = Review(
            content=review['content'],
            rate=review['rate'],
            like=review['like'],
            movie=movie,
            user=request.user
        )
        review_new.save()
        serializer = ReviewSerializer(review_new)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_delete_review(request, movie_pk):

    return Response(True)