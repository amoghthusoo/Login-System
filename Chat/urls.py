from django.urls import path
from . import views

urlpatterns = [
    path("chat", views.chat, name = "chat"),
    path("get_messages", views.get_messages, name = "get_messages")
]