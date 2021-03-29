from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.note, name="note"),
    path("", views.home, name='home'),
    path("base/", views.base, name="base"),
    path("create/", views.create, name="create")
]