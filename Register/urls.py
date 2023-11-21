from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("Register/login", views.login, name = "login"),
    path("Register/signup", views.signup, name = "signup"),
    path("Register/logout", views.logout, name = "logout"),
    path("Register/delete_account", views.delete_account, name = "delete_account")
]