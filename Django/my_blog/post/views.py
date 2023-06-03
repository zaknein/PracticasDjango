from django.shortcuts import render
from .models import Autor, Entrada


def queries(req):
    # obtener todos los elementos
    autores = Autor.objects.all()
    
    # objtener los datos filtrando por condicion
    filtered = Autor.objects.filter(email="andersonmary@example.net")

    # obtener un unico resultado

    autor = Autor.objects.get(id=2)

    #  Obtener los 10 primeros elementos

    limit = Autor.objects.all()[:10]

    # obtener los 10 primeros saltando los primeros 5
     
    offset =Autor.objects.all()[5:10]

    #  Obtener todos los elementos ordenados 

    orden = Autor.objects.all().order_by('email')

    # obrener todos los elementos de id menor o igual a 15

    filtrados = Autor.objects.filter(id__lte=15)
    # obtener todos los que contienen palabra yes en su nombre

    filtro3 = Autor.objects.filter(name__contains="yes")
    return render(req,'post/queries.html',{'filtro3': filtro3 ,'autores': autores, 'filtered' : filtered, 'autor': autor, 'limit': limit, 'offset':offset, 'orden':orden, 'filtrados': filtrados})