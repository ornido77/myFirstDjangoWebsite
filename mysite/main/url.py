from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.note, name="note"),
    path("home/", views.home, name='home'),
    path("create/", views.create, name="create")
]