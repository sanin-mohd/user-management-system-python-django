
from django import http
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils.functional import empty
from . models import profile
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required


dbtable=profile.objects.all()
# Create your views here.
# def login(request):
#     if request.method=="POST":
        
#         email=request.POST["email"]
#         password=request.POST["password"]
#         for userdata in dbtable:
#             if userdata.email==email and userdata.password==password:
#                 return render(request,'home.html',{'userdata':userdata})

#         return redirect('/')
#     else:
#         return render(request,'login.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('home')
        
            
            # for userdata in dbtable:
                
            #     if userdata.name==username :
            #         if not userdata.status:
            #             messages.info(request,"You are blocked by admin")
            #             return redirect('/')
            #         else:
            #             auth.login(request,user)
            #             return render(request,'home.html',{'userdata':userdata})
               

        else:
            messages.info(request,"Incorrect username or password")
            return redirect('/')
    return render(request,'login.html')
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        username=request.user
        print(username)
        
        for userdata in dbtable:
            if userdata.name==str(username):
                return render(request,'home.html',{'userdata':userdata})
    else:
        return redirect('login')           
        
    


    
    
def signup(request):
    if request.method=='POST':
        userdata=profile()
        userdata.name=request.POST['username']
        userdata.email=request.POST['email']
        userdata.password=request.POST['password']
        cpassword=request.POST['cpassword']
        userdata.career=request.POST['career']
        userdata.img=request.FILES['img']
        if(profile.objects.filter(name=userdata.name).exists()):
            messages.info(request,"An Error Occurred: Username is taken")
            print("Username is taken")
            return redirect('signup')
        elif(profile.objects.filter(email=userdata.email).exists()):
            messages.info(request,"An Error Occurred: Email ID is taken")
            print("Email ID is taken")
            return redirect('signup')
        
        if(cpassword == userdata.password):
            userdata.status=1
            userdata.save()
            user=User.objects.create_user(username=userdata.name,password=userdata.password,email=userdata.email,is_active=1,is_staff=0)
            user.save()
            auth.login(request,user)
            
            print("user created")
        else:
            messages.info(request,"An Error Occurred: Password not matching")
            print("Password not matching")
            return redirect('signup')
        
        
        return redirect('login')
    else:
        return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return redirect('login')