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
                ('precio', models.IntegerField(verbose_name=b'Precio del Producto')),
            ],
        ),
    ]
