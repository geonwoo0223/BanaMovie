from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies),
    path('genre/', views.getGenre),
    path('recommend/', views.recommendMovie),
    path('add/', views.addMovie),
    path('<int:movie_id>/', views.movieDetail),
    path('<int:movie_pk>/review/', views.get_add_review),
    path('<int:movie_pk>/review/update/', views.update_delete_review),
    
]