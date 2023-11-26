from django.urls import path
from . import views

urlpatterns = [
    path("friends", views.friends, name = "friends"),
    path("requests", views.requests, name = "requests"),
    path("send_request", views.send_request, name = "send_request"),
    path("remove/<str:target>", views.remove, name = "remove"),
    path("accept/<str:source_user>", views.accept, name = "accept"),
    path("reject/<str:source_user>", views.reject, name = "reject"),

]