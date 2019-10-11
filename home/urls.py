from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('RegistroServicio/', views.RegistroServicio, name='RegistroServicio'),
    path('buscarServicios/', views.buscarServicios, name='buscarServicios'),
    path('get_services_request/', views.get_services_request, name = 'get_services_request'),
    path('get_typeservices_request/', views.get_typeservices_request, name = 'get_typeservices_request'),

    
]