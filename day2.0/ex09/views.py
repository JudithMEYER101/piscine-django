from django.http import HttpResponse
from django.shortcuts import render
from .models import People


def display(request):
    try:
        people = People.objects.filter(
            homeworld__climate__icontains="windy"
        ).order_by("name")

        if len(people) == 0:
            return HttpResponse(
                "No data available, please use the following command line before use:<br>"
                "python3 manage.py loaddata ex09_initial_data.json"
            )

        return render(request, "ex09/display.html", {
            "people": people,
        })

    except Exception:
        return HttpResponse(
            "No data available, please use the following command line before use:<br>"
            "python3 manage.py loaddata ex09_initial_data.json"
        )