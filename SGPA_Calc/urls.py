from django.urls import path
from . import views

urlpatterns = [
    path("calculate_save", views.calculate_save, name="calculate_save"),
    path("records", views.records, name="records") 
]