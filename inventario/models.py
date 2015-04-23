from django.db import models
from django.contrib.auth.models import User


# Create your models here.
'''
	ID: int [100]
	Nombre: string [100]
	Cantidad: int [100]
	Imagen: jpg
	Precio: int [100]
	Descripcion: string [100]
'''
class Producto(models.Model):
	nombre_producto = models.CharField(max_length=30, verbose_name='Nombre del Producto', unique=True)
	descripcion = models.TextField(verbose_name='Descripcion')
	imagen = models.ImageField(upload_to='productos', verbose_name='Imagen')
	min_stock = models.IntegerField(verbose_name='Cantidad Minima en Stock')
	max_stock = models.IntegerField(verbose_name='Cantidad Maxima en Stock')
	precio = models.IntegerField(verbose_name='Precio del Producto')

	def __unicode__(self):
		return self.nombre_producto
	
