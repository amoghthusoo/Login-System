from django.urls import path
from . import views

urlpatterns = [
    path("chat", views.chat, name = "chat"),
    path("get_messages", views.get_messages, name = "get_messages"),
    path("put_message", views.put_message, name = "put_message"),
    path("clear", views.clear, name = "clear")
]