# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-11-12 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0041_auto_20171112_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planctto',
            name='BiderCttoPlan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
