from django.urls import path
from . import views

urlpatterns = [
    
    path("friends", views.friends, name = "friends"),
    path("requests", views.requests, name = "requests"),
    path("send_request", views.send_request, name = "send_request"),
    path("remove/<str:target>", views.remove, name = "remove"),
    path("accept/<str:source_user>", views.accept, name = "accept"),
    path("reject/<str:source_user>", views.reject, name = "reject"),
    path("dm/<str:source_user>/<str:dest_user>", views.dm, name = "dm"),
    path("get_dms", views.get_dms, name = "get_dms"),
    path("put_dm", views.put_dm, name = "put_dm"),
    path("clear_chat/<str:dest_user>", views.clear_chat, name = "clear_chat"),

]