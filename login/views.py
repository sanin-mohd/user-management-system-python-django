
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


def login_page(request):
    
    if request.session.has_key('user')and profile.objects.get(name=request.session['user']).status:
        return redirect('home')
    if request.method=="POST":
        
        username=request.POST["username"]
        password=request.POST["password"]
        dbtable=profile.objects.all()
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            userdata=profile.objects.get(name=username)
            if userdata.status:
                
                
                request.session['user']=user.username
                print(user.username)
                return redirect('home')
            else:
                messages.info(request,"You are blocked by admin")
                return redirect('/')

        else:
            messages.info(request,"Incorrect username or password")
            return redirect('/')
    return render(request,'login.html')

def home(request):
    if request.session.has_key('user') and profile.objects.get(name=request.session['user']).status:
        username=request.session['user']
        print(username)
        userdata=profile.objects.get(name=username)
        return render(request,'home.html',{'userdata':userdata})
    else:
        
        return redirect('login')           
        
    


    
    
def signup(request):
    if request.session.has_key('user'):
        return redirect('home')
    if request.method=='POST':
        userdata=profile()
        userdata.name=request.POST['username']
        userdata.email=request.POST['email']
        userdata.password=request.POST['password']
        cpassword=request.POST['cpassword']
        userdata.career=request.POST['career']
        userdata.img=request.FILES['img']
        if(profile.objects.filter(name=userdata.name).exists() or User.objects.filter(username=userdata.name).exists()):
            messages.info(request,"An Error Occurred: Username is taken")
            print("Username is taken")
            return redirect('signup')
        elif(profile.objects.filter(email=userdata.email).exists() or User.objects.filter(username=userdata.name).exists()):
            messages.info(request,"An Error Occurred: Email ID is taken")
            print("Email ID is taken")
            return redirect('signup')
        
        if(cpassword == userdata.password):
            userdata.status=1
            userdata.save()
            user=User.objects.create_user(username=userdata.name,password=userdata.password,email=userdata.email,is_active=1,is_staff=0)
            user.save()
            
            request.session['user']=userdata.name
            
            print("user created")
            return redirect('home')
        else:
            messages.info(request,"An Error Occurred: Password not matching")
            print("Password not matching")
            return redirect('signup')
        
        
        return redirect('login')
    else:
        return render(request,'signup.html')
def logout(request):
    
    del request.session['user']
    
    
    print("logout")
    return redirect('home')
    