from django.urls import path
from . import views

urlpatterns = [
    path("synchronize/<str:data>", views.synchronize, name = "synchronize"),
    path("get_X", views.get_X, name = "get_X"),
    path("get_O", views.get_O, name = "get_O"),
    path("put_X/<str:data>", views.put_X, name = "put_X"),
    path("put_O/<str:data>", views.put_O, name = "put_O"),
    path("reset", views.reset, name = "reset")
]