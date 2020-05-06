from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'user/login.html')

def profile(request):
    return render(request,'user/profile.html')

def submit(request):
    return render(request,'user/submit.html')

def admin(request):
    return render(request,'user/admin.html')

def donate(request):
    return render(request,'user/donate.html')

def dispose(request):
    return render(request,'user/disposal.html')