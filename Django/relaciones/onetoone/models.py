from django.db import models


class Lugar(models.Model):
    name = models.CharField(max_length=50)
    andress = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurante(models.Model):
    lugar = models.OneToOneField(Lugar, on_delete = CASCADE, primary_key=True)
    n_empleados = models.IntegerField(default=1)   

    def __str__(self):
        return self.place.name