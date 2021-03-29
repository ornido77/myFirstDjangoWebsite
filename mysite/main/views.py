from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Names, notes
from .forms import createNewNote

# Create your views here.

def note(response, id):
    ls = Names.objects.get(id=id)
    return render(response, 'main/notes.html', {"varNote":ls})

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == "POST":
        form = createNewNote(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Names(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = createNewNote()
    return render(response, 'main/create.html', {"varForm":form})