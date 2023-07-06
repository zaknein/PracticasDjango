from django.shortcuts import render
from django.http import HttpResponse
from .forms import ComentForm

def index(request):
    return render(request, 'index.html', {})
    

def form(request):
    coment_form = ComentForm()
    return render (request, 'form.html', {'coment_form': coment_form})

def goal(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['name'])