from django.shortcuts import render
from .forms import SearchForm
from .models import Movies


def index(request):
    form = SearchForm()
    results = None

    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            min_date = form.cleaned_data["min_date"]
            max_date = form.cleaned_data["max_date"]
            diameter = form.cleaned_data["diameter"]
            gender = form.cleaned_data["gender"]

            movies = Movies.objects.filter(
                release_date__range=(min_date, max_date),
                characters__gender=gender,
                characters__homeworld__diameter__gte=diameter
            ).select_related().prefetch_related(
                "characters",
                "characters__homeworld"
            ).distinct().order_by("title")

            results = []

            for movie in movies:
                characters = movie.characters.filter(
                    gender=gender,
                    homeworld__diameter__gte=diameter
                )

                for character in characters:
                    results.append({
                        "movie": movie,
                        "character": character,
                        "planet": character.homeworld,
                    })

    return render(request, "ex10/index.html", {
        "form": form,
        "results": results,
    })