from django.urls import path
from notebooks.views import authentication
from notebooks.views import home

urlpatterns = [
    # path("", views.index, name="notebook_index"),
    path("login/", authentication.Login.as_view(), name="login"),
    path("register/", authentication.Register.as_view(), name="register"),
]
