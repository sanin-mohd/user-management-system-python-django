
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import profile
dbtable=profile.objects.all()
# Create your views here.
def login_page(request):
    return render(request,'login.html')
def home(request):

    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        for userdata in dbtable:
            if userdata.email==email and userdata.password==password:
                return render(request,'home.html',{'userdata':userdata})

        return redirect('/')
    else:
        return redirect('/')
def signup(request):
    return render(request,'signup.html')