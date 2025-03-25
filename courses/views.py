from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Big_Data(request):
    return render(request, 'courses/Big_Data.html')
def Data_Analysis(request):
    return render(request, 'courses/Data_Analysis.html')

def Data_Science(request):
    return render(request, 'courses/Data_Science.html')

def Deep_Learning(request):
    return render(request, 'courses/Deep_Learning.html')
    