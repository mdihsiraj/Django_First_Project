from django.urls import path
from .import views

urlpatterns = [
    path('fc/', views.free_courses),
    path('bg/', views.blog),
]