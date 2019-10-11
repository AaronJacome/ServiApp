from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def RegistroServicio(request):
    return render(request, 'home/RegistroServicio.html')    
def buscarServicios(request):
    return render(request, 'home/buscarServicios.html')
