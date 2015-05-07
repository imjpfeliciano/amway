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
	
'''
	NombreEmpresa: string [100]
	Fecha: date
	Cuenta: int[100]
	Nombre: string[100]
	RFC: string[13]
	SaldoInicial: int[100]
	Cargos: int[100]
	Abonos: int[100]
	SaldoActual: int[100]
'''	
class Reporte(models.Model):
	nombre_empresa = models.CharField(max_length=40, verbose_name='Nombre de la Empresa')
	fecha = models.DateField(verbose_name='Fecha')
	cuenta = models.IntegerField(verbose_name='Nro. de Cuenta')
	nombre = models.CharField(max_length=20, verbose_name='Nombre')
	rfc = models.CharField(max_length=20, verbose_name='RFC')
	saldo_inicial = models.IntegerField(verbose_name='Saldo Inicial')
	cargos = models.IntegerField(verbose_name='Cargos')
	abonos = models.IntegerField(verbose_name='Abonos')
	saldo_actual = models.IntegerField(verbose_name='Saldo Actual')

	def __unicode__(self):
		return self.rfc


