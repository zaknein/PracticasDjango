from django.db import models

    
class Salary(models.Model):
    cantidad = models.IntegerField()
    aguinaldo_jun = models.BooleanField()
    aguinaldo_dic = models.BooleanField()

class Job(models.Model):
    titulo = models.CharField(max_length=20, null=False)
    descripcion = models.TextField(max_length= 200)
    salario = models.ManyToManyField(Salary)

class Country(models.Model):
    nombre = models.CharField(max_length=20,null=False)
    country_code = models.IntegerField(null = False)
    
class Location(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    country = models.ManyToManyField(Country)
    
class Place(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    direccion = models.CharField(max_length=30, null= False)
    codigo_postal = models.IntegerField()
    location = models.ManyToManyField(Location)
    

class Empleado(models.Model):
    nombre = models.CharField(max_length= 20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50, null=False)
    job = models.ManyToManyField(Job)
    place =models.ManyToManyField(Place)

    def __str__(self):
        return self.nombre