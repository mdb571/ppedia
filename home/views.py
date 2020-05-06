from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home/home.html')

def get_started(request):
    return render(request,'home/started.html')

def masks(request):
    return render(request,'home/masks.html')

def gloves(request):
    return render(request,'home/gloves.html')

def boots(request):
    return render(request,'home/boots.html')

def goggles(request):
    return render(request,'home/goggles.html')

def gowns(request):
    return render(request,'home/gown.html')