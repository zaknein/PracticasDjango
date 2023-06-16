from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo, Publicacion

def crear(req):
    # para relacionarlos, ambos objetos deben estar guardados
    # art1 = Articulo(titular='primer 1 ')
    # art1.save()
    # art2 = Articulo(titular='primer 2 ')
    # art2.save()
    # art3 = Articulo(titular='primer 3 ')
    # art3.save()

    # pub1 = Publicacion(titulo='publik 1')
    # pub1.save()
    # pub2 = Publicacion(titulo='publik 2')
    # pub2.save()
    # pub3 = Publicacion(titulo='publik 3')
    # pub3.save()


    # art1.publicaciones.add(pub1)
    # art2.publicaciones.add(pub2)
    # art3.publicaciones.add(pub3)

    pub9= Publicacion.objects.get(id=2)
    result= pub9.articulo_set.all()
    # result = art1.publicaciones.all()


    return HttpResponse(result)


