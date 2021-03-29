from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Names, notes
from .forms import createNewNote

# Create your views here.

def note(response, id):
    ls = Names.objects.get(id=id)
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.notes_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()
        elif response.POST.get("new"):
            txt = response.POST.get("newNote")

            if len(txt) > 5:
                ls.notes_set.create(text=txt, complete=False)
            else:
                print("invalid")
    return render(response, 'main/notes.html', {"varName":ls})

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

def base(response):
    return render(response, 'main/base.html', {})