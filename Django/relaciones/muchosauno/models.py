from django.db import models


class Reportero(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.email

# para hacer una vinculacion muchos a uno,
# el elemento que solo tiene uno del otro es el que tiene la clave foranea
# como un articulo solo puede tener un reportero, es el que tiene que tener la relacion

class Articulo(models.Model):
    titular = models.CharField(max_length=30)
    fecha = models.DateField()
    reportero = models.ForeignKey(Reportero, on_delete=models.CASCADE)

    def __str__(self):
       return self.titular     
