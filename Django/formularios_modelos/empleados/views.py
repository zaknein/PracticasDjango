from django.shortcuts import render
from .forms import EmpleadoForm

def index(request):
    form = EmpleadoForm()
    return render(request, 'index.html', {'form': form })

