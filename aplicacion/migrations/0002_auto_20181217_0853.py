# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 08:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendedor',
            options={'verbose_name_plural': 'Vendedores'},
        ),
        migrations.AlterField(
            model_name='venta',
            name='fechaDeVenta',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
