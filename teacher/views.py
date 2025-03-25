from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Data_Science_Teacher(request):
    return render(request, 'teacher/Data_Science_Teacher.html')
def django_teacher(request):
    return render(request, 'teacher/django_teacher.html')
