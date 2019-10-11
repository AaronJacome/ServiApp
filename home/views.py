from django.shortcuts import render
from main_app.models import tb_CalendarioServicio,Tb_CatalogoServicio
from django.http import HttpResponse
from django.core.serializers import serialize 
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def RegistroServicio(request):
    return render(request, 'home/RegistroServicio.html')    

def buscarServicios(request):
    return render(request, 'home/buscarServicios.html')

def get_services_request(request):
    if request.method == "GET":
        servicios = tb_CalendarioServicio.objects.all()
        str_data = serialize('json', servicios, cls=DjangoJSONEncoder)
        response = {}
        response['message'] = 'Login correcto'
        response['code'] = '200'
        response['data'] = str_data
        return HttpResponse(json.dumps(response), content_type="application/json")

def get_typeservices_request(request):
    if request.method == "GET":
        catalogos = Tb_CatalogoServicio.objects.all()
        str_data = serialize('json', catalogos, cls=DjangoJSONEncoder)
        response = {}
        response['message'] = 'Login correcto'
        response['code'] = '200'
        response['data'] = str_data
        return HttpResponse(json.dumps(response), content_type="application/json")
