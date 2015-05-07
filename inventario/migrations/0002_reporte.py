# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_empresa', models.CharField(max_length=40, verbose_name=b'Nombre de la Empresa')),
                ('fecha', models.DateField(verbose_name=b'Fecha')),
                ('cuenta', models.IntegerField(verbose_name=b'Nro. de Cuenta')),
                ('nombre', models.CharField(max_length=20, verbose_name=b'Nombre')),
                ('rfc', models.CharField(max_length=20, verbose_name=b'RFC')),
                ('saldo_inicial', models.IntegerField(verbose_name=b'Saldo Inicial')),
                ('cargos', models.IntegerField(verbose_name=b'Cargos')),
                ('abonos', models.IntegerField(verbose_name=b'Abonos')),
                ('saldo_actual', models.IntegerField(verbose_name=b'Saldo Actual')),
            ],
        ),
    ]
