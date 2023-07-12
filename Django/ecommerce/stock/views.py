from django.shortcuts import render
from .forms import ProductForm
 
def index(request):
    if request.method == 'POST':
        # Guardar la informacion
        form1 = ProductForm(request.POST)
        if form1.is_valid():
            form1.save()

  
    form = ProductForm()
        
    return render (request,'index.html',{'form': form})
