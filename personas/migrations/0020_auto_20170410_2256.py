# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-11 01:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0019_duenoceco'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceco',
            name='IdDueno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='personas.Duenoceco'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='duenoceco',
            name='DocIdDueno',
            field=models.CharField(blank=True, choices=[('CI', 'CI'), ('Pasaporte', 'Pasaporte')], default='CI', max_length=10, null=True),
        ),
    ]
