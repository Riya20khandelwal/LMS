from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views

urlpatters = [
    path('', views.home, name="home"),
    path('login_form/', views.login_form, name="login_form"),
    path('reg_form/', views.reg_form, name="reg_form"),
    path('about/', views.about, name="about"),
    path('login/', views.loginView, name="login"),
    path('contact/', views.contact, name="contact"),
    path('logout/', views.logoutView, name="logout"),
    path('register/', views.registerView, name="register"),
    path('services/', views.services, name="services"),
    path('llchat/', views.TiseList.as_view(), name="llchat"),
    
]