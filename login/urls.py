from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/register', views.register, name='register'),
    path('login_request/', views.loginRequest, name='login_request'),
    path('register_request/', views.registerRequest, name='register_request'),
]