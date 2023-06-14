from django.shortcuts import render
from django.http import HttpResponse


def create(req):
    return HttpResponse('Funciono')
