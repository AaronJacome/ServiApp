from django.shortcuts import render
import json
from django.http import HttpResponse
from main_app.models import Tb_Usuario 
from django.core.serializers import serialize 
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.


def index(request):
    return render(request, 'login/index.html')
     # return render(request, 'RegistroServicio/demo.html')


def loginRequest(request):
    if request.method == "POST":  # os request.GET()
        # You can access the property like dict
        data = request.POST
        # Do your logic here coz you got data in `get_value`
        response = {}
        try:
            query = Tb_Usuario.objects.get(telefono=data['telefono'], password = data['password'] )          
            str_data = serialize('json', [query], cls=DjangoJSONEncoder)
            response['message'] = 'Login correcto'
            response['code'] = '200'
            response['data'] = str_data
        except Tb_Usuario.DoesNotExist:            
            response['message'] = 'No se encuentra el usuario, favor de revisar sus credenciales'
            response['code'] = '500'    

        return HttpResponse(json.dumps(response), content_type="application/json")


def register(request):
    return render(request, 'login/register.html')

def registerRequest(request):
    if request.method == "POST":  # os request.GET()
        # You can access the property like dict
        data = request.POST
        # Do your logic here coz you got data in `get_value`
        response = {}
        try:
            data = Tb_Usuario.objects.get(telefono=data['telefono'] )          
            response['message'] = 'El usuario ya existe'
            response['code'] = '500'
            response['data'] = ''
        except:            
            usuario = Tb_Usuario(telefono=data['telefono'], password=data['pass'], nombre=data['nombre'], edad=int(data['edad']), apellidoMaterno=data['apellidoMaterno'], apellidoPaterno=data['apellidoPaterno'], status=1)

            usuario.save()

            response['message'] = 'El usuario se ha creado'
            response['code'] = '200'     

        return HttpResponse(json.dumps(response), content_type="application/json")
