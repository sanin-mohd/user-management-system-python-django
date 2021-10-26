from django.shortcuts import redirect, render
from login.models import profile
from django.contrib.auth.models import User , auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    dbtable=profile.objects.all()
    if request.session.has_key('admin'):
        return render(request,'adminpanel.html',{'dbtable':dbtable})
    else:
        return redirect('admin_login')
def admin_logout(request):
    if request.session.has_key('admin'):
        del request.session['admin']
        request.session.modified = True
        print("admin session deleted")
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
# @login_required(login_url='admin_login')
def delete_user(request,pk):
    username=profile.objects.get(id=pk).name
    profile.objects.get(id=pk).delete()
    user=User.objects.get(username=username)
    user.delete()
    print("deleted")
    return redirect('admin_home')
    # for userdata in dbtable:
    #     if userdata.name==str(username):
# @login_required(login_url='admin_login')
def edit_user(request,pk):
    if request.method=='POST':
        user=profile.objects.get(id=pk)
        user1=profile.objects.get(id=pk)
        user.name=request.POST['username']
        user.email=request.POST['email']
        user.career=request.POST['career']
        user.password=request.POST['password']
        user.cpassword=request.POST['cpassword']
        user.img=request.FILES['img']
        
        
        if(profile.objects.filter(name=user.name).exists() or User.objects.filter(username=user.name).exists()):
            messages.info(request,"An Error Occurred: Username is taken")
            print("Username is taken")
            return redirect('edit_user',pk)
        elif(profile.objects.filter(email=user.email).exists()or User.objects.filter(email=user.email).exists()):
            messages.info(request,"An Error Occurred: Email ID is taken")
            print("Email ID is taken")
            return redirect('edit_user',pk)
        
        if(user.cpassword == user.password):
            user.status=1
            user.save()
            user=User.objects.get(username=user1.name)
            user.username=request.POST['username']
            user.email=request.POST['email']
            user.password=request.POST['password']
            user.save()
            print("user created")
        else:
            messages.info(request,"An Error Occurred: Password not matching")
            print("Password not matching")
            return redirect('edit_user',pk)
        
        
        return redirect('admin_home')
    else:
        userdata=profile.objects.get(id=pk)
        return render(request,'edituser.html',{'userdata':userdata})
    

def block_user(request,pk):
    userdata=profile.objects.get(id=pk)
    if userdata.status:
        userdata.status=0
        print("User status : Inactive")
    else:
        userdata.status=1
        print("User status : Active")
    return redirect('admin_home')

