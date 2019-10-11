from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('RegistroServicio/', views.RegistroServicio, name='RegistroServicio'),
    path('buscarServicios/', views.buscarServicios, name='buscarServicios'),
]