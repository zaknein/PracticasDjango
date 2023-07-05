from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})
    
def getform(request):
    return render(request, 'form.html', {})

def getgoal(request):
    if request.method != 'GET':
        return HttpResponse('You donkey piece of shit')

    name = request.GET['name']
    return render(request, 'succes.html', {'name': name})

def postform(request):
    return render(request, 'postform.html', {})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('El metodo GET no es soportado por este formulario')
    
    info = request.POST['info']
    return render(request, 'postsucces.html', { 'info':info })