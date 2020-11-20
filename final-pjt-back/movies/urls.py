from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies),
    path('genre/', views.getGenre),
    path('recommend/', views.recommendMovie),
    path('add/', views.addMovie),
    
]