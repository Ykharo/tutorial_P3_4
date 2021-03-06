# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-01 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0032_ctto_admincttoctta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ceco',
            options={'ordering': ['CodCeco']},
        ),
        migrations.AlterModelOptions(
            name='ctta',
            options={'ordering': ['NomCtta']},
        ),
        migrations.AlterModelOptions(
            name='personalctta',
            options={'ordering': ['IdCtta']},
        ),
        migrations.AddField(
            model_name='ctto',
            name='ProvisCtto',
            field=models.CharField(blank=True, choices=[('Calculada', 'Calculada'), ('Informada', 'Informada')], default='Calculada', max_length=10, null=True),
        ),
    ]
