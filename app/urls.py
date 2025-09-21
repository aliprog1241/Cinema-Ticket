from django.urls import path
from . import views



urlpatterns = [
    path('movies/', views.list_movies, name='list_movies'),
    path('movies/<int:movie_id>/seats/', views.list_seats, name='list_seats'),
    path('movies/<int:movie_id>/reserve/<int:seat_id>/', views.reserve_seat, name='reserve_seat'),
    path('stats/', views.stats, name='stats'),
]