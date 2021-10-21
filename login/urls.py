
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login'),
    path('home',views.home,name='home'),
    path('signup',views.signup)
    
]