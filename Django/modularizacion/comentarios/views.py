from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario

def test(request):
    return HttpResponse("Hola mundo")

def create(request):
    # comentario = Comentario(name="asfo",score=2,comment="este es un comentario")
    # comentario.save()
    comentario = Comentario.objects.create(name="alex")
    return HttpResponse("Ruta para probar la creacion de modulos")

def delete(req):
    # comentario = Comentario.objects.get(id=10)
    # comentario.delete()
    Comentario.objects.filter(name="alex").delete()
    return HttpResponse("ruta de comprobacion de borrados")