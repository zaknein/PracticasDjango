from django.urls import path
from . import views

urlpatterns = [
    path('queries/', views.queries, name="queries"),
    path('actualizar/', views.actualizar, name="actualizar")

]
