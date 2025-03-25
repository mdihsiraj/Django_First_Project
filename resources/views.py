from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def free_courses(request):
    return render(request, 'resources/free_course.html')
def blog(request):
    return render(request, 'resources/blog.html')
