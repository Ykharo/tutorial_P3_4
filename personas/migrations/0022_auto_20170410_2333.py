# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-11 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0021_duenoceco_cargodueno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duenoceco',
            name='CargoDueno',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
