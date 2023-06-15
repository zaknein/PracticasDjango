from django.shortcuts import render
from django.http import HttpResponse
from .models import Reportero, Articulo
from datetime import date



def crear(req):
    rep = Reportero(nombre= 'pablo', apellido='menz', email='menz@mail.com')
    rep.save()
    art= Articulo(titular='lorem impsum',fecha=date(2022,5,5),reportero=rep)
    art.save()
    art2= Articulo(titular='lre impsum',fecha=date(2023,6,5),reportero=rep)
    art2.save()
    art3= Articulo(titular='los impsum',fecha=date(2021,7,5),reportero=rep)
    art3.save()

    # result = art.reportero.nombre
    result = rep.articulo_set.all()
    return HttpResponse(result)
