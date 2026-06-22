from django.shortcuts import render


def index(request):
    shades = []

    for i in range(50):
        value = int(255 - (i * 255 / 49))

        shades.append({
            "black": f"rgb({value}, {value}, {value})",
            "red": f"rgb({value}, 0, 0)",
            "blue": f"rgb(0, 0, {value})",
            "green": f"rgb(0, {value}, 0)",
        })

    return render(request, "ex03/index.html", {
        "shades": shades,
    })