from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length= 20, null=False)
    apellido = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50, null=False)
    job = models.ForeignKey(Job, on_delete= models.CASCADE)
    place =models.ForeignKey(Place , on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Job(models.Model):
    titulo = models.CharField(max_length=20, null=False)
    descripcion = models.TextField(max_length= 200)
    salario = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
class Salary(models.Model):
    cantidad = models.IntegerField()
    aguinaldo_jun = models.BooleanField()
    aguinaldo_dic = models.BooleanField()

class Place(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    direccion = models.CharField(max_length=30, null= False)
    codigo_postal = models.IntegerField(max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Location(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
class Country(models.Model):
    nombre = models.CharField(max_length=20,null=False)
    country_code = models.IntegerField(max_length=3, null = False)
