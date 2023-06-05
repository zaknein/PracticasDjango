from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugar, Restaurante

def crear(request):
    #  TODO Crear elemento
    lugar = Lugar(name='place1', adress = 'Calle falsa 123')
    lugar.save()
    
    restaurante = Restaurante(lugar=lugar, n_empleados = 10 )
    restaurante.save()

    return HttpResponse(restaurante.lugar.name)

