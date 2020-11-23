from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies),
    path('genre/', views.getGenre),
    path('recommend/<int:user_pk>/', views.recommendMovie),
    path('add/', views.addMovie),
    path('<int:movie_pk>/', views.movieDetail),
    path('<int:movie_pk>/reviews/', views.getAllReviews),
    path('<int:movie_pk>/review/', views.get_add_review),
    path('<int:movie_pk>/review/update/', views.update_delete_review),
    
]