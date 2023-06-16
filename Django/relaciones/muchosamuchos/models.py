from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo


class Articulo(models.Model):

    titular = models.CharField(max_length=100)


    def __str__(self):
        return self.titular   