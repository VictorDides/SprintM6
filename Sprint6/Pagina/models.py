from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Publicacion(models.Model):
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    SKU = models.IntegerField()
    stock = models.IntegerField()
    proveedor = models.CharField(max_length=254)

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion,  on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(default= timezone.now)