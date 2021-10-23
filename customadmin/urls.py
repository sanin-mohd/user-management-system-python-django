
from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('adduser',views.adduser,name='adduser'),
    
    
    
]