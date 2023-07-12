from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    short_descripcion = models.CharField(max_length=100,blank=False,null=False)
    descripcion = models.TextField(blank=False, null=False)
    stock = models.IntegerField(default=20)

    def __str__(self):
        return self.name
