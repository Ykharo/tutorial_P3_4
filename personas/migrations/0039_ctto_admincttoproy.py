# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-26 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0038_personaladminproyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctto',
            name='AdminCttoProy',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='personas.PersonalAdminProyecto'),
        ),
    ]
