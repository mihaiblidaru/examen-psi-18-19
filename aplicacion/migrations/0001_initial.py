# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreP', models.CharField(blank=True, max_length=128, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreV', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDeVenta', models.DateField()),
                ('prenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Prenda')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.Vendedor')),
            ],
        ),
    ]