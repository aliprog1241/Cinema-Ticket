from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseForbidden
from django.urls import reverse
from django.db.models import Count
from .models import Movie, Seat, Ticket

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, 'app/movies.html', {'movies': movies})

def list_seats(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reserved_seats = Ticket.objects.filter(movie=movie).values_list('seat_id', flat=True)
    available_seats = Seat.objects.exclude(id__in=reserved_seats)
    return render(request, 'app/seats.html', {
        'movie': movie,
        'seats': available_seats
    })

@login_required
def reserve_seat(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    seat = get_object_or_404(Seat, pk=seat_id)


    if Ticket.objects.filter(movie=movie, seat=seat).exists():
        return redirect('list_seats', movie_id=movie.id)

    Ticket.objects.create(movie=movie, seat=seat, user=request.user)
    return redirect('list_seats', movie_id=movie.id)

@user_passes_test(lambda u: u.is_superuser)
def stats(request):
    data = (
        Ticket.objects
        .values('seat__number')
        .annotate(total=Count('id'))
        .order_by('seat__number')
    )
    return JsonResponse({"stats": list(data)})
