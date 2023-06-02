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
    return render(req,'post/queries.html',{'autores': autores, 'filtered' : filtered, 'autor': autor, 'limit': limit, 'offset':offset})