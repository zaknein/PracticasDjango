from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def material(request):
    return render (request,'material.html',{})