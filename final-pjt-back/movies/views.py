import requests

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieSerializer
from .models import Movie, Genre


# Create your views here.
# @api_view(['POST'])
# def createMovie(request):
#     movies = request.data
#     serializer_data = []
    # for movie in movies:
    #     temp = movie["genres"]
    #     movie["genres"] = []
    #     for i in temp :
    #         mygenre = Genre.objects.get(pk=i)
    #         movie["genres"].append(mygenre.name)
    #     print(movie["genres"], ',')
        
    #
    #     serializer = MovieSerializer(data=movie)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer_data.append(serializer.data)
    # print("="*50)
    # print(serializer_data)
    # print("="*50)


    # return Response()

def getMovies(request):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key=e8067ff017c9f1acd66ea2924205aae6'
    payload = {
        'language' : 'ko'
    }
    r = requests.get(url, params=payload)
    movies = r.json()
    for movie in movies['results']:
        print(movie)
        movie_new = Movie(
            movie_no= movie['id'],
            title= movie['title'],
            release_date= movie['release_date'],
            poster_path= movie['poster_path'],
            adult= movie['adult'],
            overview= movie['overview'],
            # genres= movie['genre_ids']
        )
        movie_new.save()
        # print(movie_new)
        # print(movie_new.id)

        for genre in movie['genre_ids']:
            movie_new.genres.add(genre)
        
        # movie_genre = Genre.objects.fliter(movie_id=movie_new.id)
        # movie_new.genres.set(movie_genre)
        
        # if movie_new.is_valid():
            # movie_temp = movie_new.save(commit=False)
            # movie_temp.genres = movie_genres.objects.all().filter(movie_id=movie_new_pk)
            # movie_temp.save()
            # movie_new.save()
    
        

        # data = {
        #     'movie_no': movie.id
        #     'title': movie.title,
        #     'release_date': movie.release_date,
        #     'poster_path': movie.poster_path,
        #     'adult': movie.adult,
        #     'overview': movie.overview,
        #     'genres': 
        # }
    return Response(Movie.objects.all())
    

