from django.urls import path
from . import views


urlpatterns = [
    path('', views.board_list_create),
    path('<int:board_pk>/', views.board_detail),

]