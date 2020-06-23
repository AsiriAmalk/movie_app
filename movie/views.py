from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages


def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {"search_result": search_result}
    return render(request, 'movies/moveis_stuff.html', stuff_for_frontend)


def create(request):
    if request.method == "POST":
        try:

            value = request.POST

            movie = Movie(name=value.get('name'),
                          picture=value.get('url'),
                          rating=value.get('rate'),
                          notes=value.get('description'),
                          )
            movie.save()
            messages.success(request, "New movie added {}".format(movie.name))
        except Exception as e:
            messages.warning(request, "Got an error while create a new movie {}".format(e))

    return redirect('/')


def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            movie_obj = Movie.objects.get(id=movie_id)
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()
            messages.success(request, "Movie Updated {}".format(movie_obj.name))
        except Exception as e:
            messages.warning(request, "Got an error while updating the movie {}".format(e))
    return redirect('/')


def delete(request, movie_id):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
        movie_obj.delete()
        messages.success(request, "Movie deleted {}".format(movie_obj.name))
    except Exception as e:
        messages.warning(request, "Got an error while deleting the movie {}".format(e))
    return redirect("/")
