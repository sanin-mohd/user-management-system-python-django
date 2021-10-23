from django.shortcuts import redirect, render
from login.models import profile
from django.contrib.auth.models import User , auth

dbtable=profile.objects.all()

# Create your views here.
def admin_login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if(username=="admin" and password=="admin"):
            return render(request,'adminpanel.html',{'dbtable':dbtable})
        else:
            return redirect('/')
    else:
        return render(request,'admin.html')