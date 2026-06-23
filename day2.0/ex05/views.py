from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies


def get_movies():
    return [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19",
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16",
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19",
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25",
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kutz, Rick McCallum",
            "release_date": "1980-05-17",
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25",
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11",
        },
    ]


def populate(request):
    results = []

    for movie in get_movies():
        try:
            Movies.objects.update_or_create(
                episode_nb=movie["episode_nb"],
                defaults=movie,
            )
            results.append("OK")
        except Exception as error:
            results.append(str(error))

    return HttpResponse("<br>".join(results))


def display(request):
    try:
        movies = Movies.objects.all().order_by("episode_nb")

        if len(movies) == 0:
            return HttpResponse("No data available")

        return render(request, "ex05/display.html", {
            "movies": movies,
        })

    except Exception:
        return HttpResponse("No data available")


def remove(request):
    try:
        if request.method == "POST":
            title = request.POST.get("title")

            if title:
                Movies.objects.filter(title=title).delete()

            return redirect("/ex05/remove")

        movies = Movies.objects.all().order_by("episode_nb")

        if len(movies) == 0:
            return HttpResponse("No data available")

        return render(request, "ex05/remove.html", {
            "movies": movies,
        })

    except Exception:
        return HttpResponse("No data available")