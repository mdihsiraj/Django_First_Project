from django.urls import path
from .import views

urlpatterns = [
    path('bd/', views.Big_Data),
    path('da/', views.Data_Analysis),
    path('ds/', views.Data_Science),
    path('dl/', views.Deep_Learning),
]