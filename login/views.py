from django.shortcuts import render
import json
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'login/index.html')
     # return render(request, 'RegistroServicio/demo.html')

def login(request):
    if request.method == "POST": #os request.GET()
        print(request.POST)
        #You can access the property like dict
        data = request.POST
        # Do your logic here coz you got data in `get_value`
        data = {}
        data['result'] = 'you made a request'
        return HttpResponse(json.dumps(data), content_type="application/json")