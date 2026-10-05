from django.shortcuts import render
from django.urls import path
# Create your views here.

def education(request):
    return render(request,'education/index.html')