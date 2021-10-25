from django.shortcuts import redirect, render
from login.models import profile
from django.contrib.auth.models import User , auth
from django.contrib import messages

dbtable=profile.objects.all()

# Create your views here.
def admin_login(request):
    if request.session.has_key('admin'):
        return redirect('admin_home')
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if(username=="admin" and password=="admin"):
            request.session['admin']='admin'
            return redirect('admin_home')
        else:
            return redirect('admin_login')
    else:
        return render(request,'admin.html')
def admin_home(request):
    if request.session.has_key('admin'):
        return render(request,'adminpanel.html',{'dbtable':dbtable})
    else:
        return redirect('admin_login')
def admin_logout(request):
    if request.session.has_key('admin'):
        request.session.flush()
        return redirect('admin_login')
def adduser(request):
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
            return redirect('adduser')
        elif(profile.objects.filter(email=userdata.email).exists()):
            messages.info(request,"An Error Occurred: Email ID is taken")
            print("Email ID is taken")
            return redirect('adduser')
        
        if(cpassword == userdata.password):
            userdata.status=1
            userdata.save()
            inbuilt_user_tb=User.objects.create_user(username=userdata.name,password=userdata.password,email=userdata.email,is_active=1,is_staff=0)
            inbuilt_user_tb.save()
            print("user created")
        else:
            messages.info(request,"An Error Occurred: Password not matching")
            print("Password not matching")
            return redirect('adduser')
        
        
        return redirect('admin_home')
    else:
        return render(request,'adduser.html')

def delete_user(request):
    pass
    # for userdata in dbtable:
    #     if userdata.name==str(username):


