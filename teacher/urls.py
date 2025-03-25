from django.urls import path
from .import views

urlpatterns = [
    path('dst/', views.Data_Science_Teacher),
    path('dt/', views.django_teacher),
    
]