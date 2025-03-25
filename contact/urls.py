from django.urls import path
from .import views

urlpatterns = [
    path('cn/', views.contact),
]