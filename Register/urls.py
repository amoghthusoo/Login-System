from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("Register/login.html", views.login, name = "login"),
    path("Register/signup.html", views.signup, name = "signup"),
    path("Register/logout", views.logout, name = "logout")
]