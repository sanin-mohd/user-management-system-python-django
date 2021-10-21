
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import a,b

# Create your views here.
def login_page(request):
    return render(request,'login.html')
def home(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        if(email in (a.email,b.email) and password=="1234"):
            return render(request,'home.html',{'data':a})

    
        return redirect('/')
    else:
        return redirect('/')
def signup(request):
    return render(request,'signup.html')