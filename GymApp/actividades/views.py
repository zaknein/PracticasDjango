from django.shortcuts import render
from django.http import HttpResponse

def act(request):
    return HttpResponse('vive act') 