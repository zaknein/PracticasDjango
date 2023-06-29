from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})
    
def form(request):
    return render(request, 'form.html', {})

def goal(request):
    if request.method != 'GET':
        return HttpResponse('You donkey piece of shit')

    name = request.GET['name']
    return render(request, 'succes.html', {'name': name})