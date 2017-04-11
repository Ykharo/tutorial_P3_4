# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-11 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0018_itemodc_totalitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duenoceco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomDueno', models.CharField(max_length=20)),
                ('DocIdDueno', models.CharField(blank=True, choices=[('CI', 'CI'), ('Rut', 'Rut')], default='CI', max_length=10, null=True)),
                ('NumDocDueno', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
