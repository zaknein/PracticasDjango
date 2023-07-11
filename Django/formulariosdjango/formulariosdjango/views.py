from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentForm, ContactForm

def index(request):
    return render(request, 'index.html', {})
    

def form(request):
    coment_form = ComentForm()
    return render (request, 'form.html', {'coment_form': coment_form})

def goal(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['name'])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()  
        return render(request,'widget.html',{'form':form})
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aqui irian todas las acciones a realizar cuando los datos son correctos
            return HttpResponse('valido')
        else:
            #  Comunicamos al usuario que los datos no son validos o cosas asi 
            return render(request,'widget.html',{'form':form})

