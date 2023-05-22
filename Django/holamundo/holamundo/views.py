from django.http import HttpResponse

def saludo(request):
    return HttpResponse('Hola Mundo')

def despedida(request):
    return HttpResponse('Nos vemos en Tokyo')    

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse('Es mayor de edad')
    else :
        return HttpResponse('Es menor de edad')    
