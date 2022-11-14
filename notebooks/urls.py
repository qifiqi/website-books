from django.urls import path
from notebooks.views import authentication

urlpatterns = [
    # path("", views.index, name="notebook_index"),
    path("login/", authentication.Login.as_view(), name="login"),
    path("register/", authentication.Register.as_view(), name="register"),

]
