from django.shortcuts import render

from web.models import Tarifas


# Create your views here.

def Home(request):

    #usando el modelo para traer datos
    tarifas=Tarifas.objects.all()

    #crear un diccionario con los datos a enviar
    diccionario={
        'tarifas':tarifas
    }

    print(diccionario)
    return render(request,'index.html',diccionario) 

def Tarifa(request):
    return render(request,'tarifas.html')