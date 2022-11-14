from django.urls import path
from notebooks import views

urlpatterns = [
    path("", views.index, name="notebook_index"),
]
