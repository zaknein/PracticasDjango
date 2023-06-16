from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

# para hacer una relacion muchos a muchos
# hay que declararlo en una de las dos clases implicadas,
# no hace falta en ambas

class Articulo(models.Model):

    titular = models.CharField(max_length=100)
    publicaciones = models.ManyToManyField(Publicacion)
    # solo necesita el modelo,
    # no es necesario un metodo de borrado, 
    # puesto que se crea una tercer table


    def __str__(self):
        return self.titular
