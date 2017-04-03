# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-01 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0014_auto_20170319_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='edp',
            name='AnticipoEDP',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='DescuentoEDP',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AlterField(
            model_name='ctto',
            name='AdjudicCtto',
            field=models.CharField(blank=True, choices=[('Directa', 'Directa'), ('Cotizaciones', 'Cotizaciones'), ('Licitación', 'Licitación')], default='Directa', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ctto',
            name='MonedaCtto',
            field=models.CharField(blank=True, choices=[('CLP', 'CLP'), ('USD', 'USD'), ('UF', 'UF'), ('EUR', 'EUR'), ('CAD', 'CAD')], default='CLP', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='ctto',
            name='SeguroCtto',
            field=models.CharField(blank=True, choices=[('Si', 'Aplica Seguro'), ('No', 'No Aplica Seguro')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ctto',
            name='TerrenCtto',
            field=models.CharField(blank=True, choices=[('Si', 'Con Terreno'), ('No', 'Sin Terreno')], default='No', max_length=10, null=True),
        ),
    ]
