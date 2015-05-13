# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=40, verbose_name=b'Nombre de usuario')),
                ('password', models.CharField(max_length=40, verbose_name=b'Contrase\xc3\xb1a')),
            ],
        ),
    ]
