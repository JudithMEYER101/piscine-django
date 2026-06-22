from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from .forms import TextForm


def read_history():
    try:
        file = open(settings.LOG_FILE, "r")
        history = file.readlines()
        file.close()
        return history
    except FileNotFoundError:
        return []


def write_history(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = timestamp + " - " + text + "\n"

    file = open(settings.LOG_FILE, "a")
    file.write(line)
    file.close()


def index(request):
    if request.method == "POST":
        form = TextForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data["text"]
            write_history(text)
            form = TextForm()
    else:
        form = TextForm()

    history = read_history()

    return render(request, "ex02/index.html", {
        "form": form,
        "history": history,
    })