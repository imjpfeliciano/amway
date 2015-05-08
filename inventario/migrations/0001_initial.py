# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_producto', models.CharField(unique=True, max_length=30, verbose_name=b'Nombre del Producto')),
                ('descripcion', models.TextField(verbose_name=b'Descripcion')),
                ('imagen', models.ImageField(upload_to=b'productos', verbose_name=b'Imagen')),
                ('min_stock', models.IntegerField(verbose_name=b'Cantidad Minima en Stock')),
                ('max_stock', models.IntegerField(verbose_name=b'Cantidad Maxima en Stock')),
                ('in_stock', models.IntegerField(verbose_name=b'Stock Actual')),
                ('precio', models.IntegerField(verbose_name=b'Precio del Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_empresa', models.CharField(max_length=40, verbose_name=b'Nombre de la Empresa')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name=b'Fecha')),
                ('cuenta', models.IntegerField(verbose_name=b'Nro. de Cuenta')),
                ('nombre', models.CharField(max_length=20, verbose_name=b'Nombre')),
                ('rfc', models.CharField(max_length=20, verbose_name=b'RFC')),
                ('saldo_inicial', models.IntegerField(verbose_name=b'Saldo Inicial')),
                ('cargos', models.IntegerField(verbose_name=b'Cargos')),
                ('abonos', models.IntegerField(verbose_name=b'Abonos')),
                ('saldo_actual', models.IntegerField(verbose_name=b'Saldo Actual')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_usuario', models.CharField(unique=True, max_length=30, verbose_name=b'Usuario')),
                ('email', models.CharField(unique=True, max_length=30, verbose_name=b'email')),
                ('password', models.CharField(max_length=30, verbose_name=b'Contrase\xc3\xb1a')),
                ('tipo_usuario', models.IntegerField(verbose_name=b'Tipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
