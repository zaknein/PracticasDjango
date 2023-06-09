from django.urls import path
from . import  views


urlpatterns = [
    path('actividades/', views.act , name ='actividades')
]