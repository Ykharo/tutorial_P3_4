# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-11-11 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0039_ctto_admincttoproy'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanCtto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdCodePlan', models.CharField(max_length=20)),
                ('CecoPlan', models.CharField(blank=True, max_length=50, null=True)),
                ('AreaPlan', models.CharField(blank=True, max_length=50, null=True)),
                ('CarpetAplan', models.CharField(blank=True, max_length=30, null=True)),
                ('CodCttoPlan', models.CharField(blank=True, max_length=20, null=True)),
                ('TipoDocPlan', models.CharField(blank=True, max_length=30, null=True)),
                ('NombCttoPlan', models.CharField(blank=True, max_length=100, null=True)),
                ('DescCttoPlan', models.CharField(blank=True, max_length=100, null=True)),
                ('CategoriCttoPlan', models.CharField(blank=True, max_length=10, null=True)),
                ('ModalidadCttoPlan', models.CharField(blank=True, max_length=10, null=True)),
                ('FechIniFlujCttoplan', models.DateField(null=True)),
                ('FechTerFlujCttoplan', models.DateField(null=True)),
                ('AsignaCttoPlan', models.CharField(blank=True, max_length=30, null=True)),
                ('OrigenCttoPlan', models.CharField(blank=True, max_length=20, null=True)),
                ('MOLocalCttoPlan', models.CharField(blank=True, max_length=10, null=True)),
                ('TerrenoCttoPlan', models.CharField(blank=True, max_length=10, null=True)),
                ('TitleCttoPlan', models.CharField(blank=True, max_length=100, null=True)),
                ('DetailCttoPlan', models.CharField(blank=True, max_length=150, null=True)),
                ('BidProcessCttoPlan', models.CharField(blank=True, max_length=50, null=True)),
                ('BiderCttoPlan', models.CharField(blank=True, max_length=30, null=True)),
                ('FechEspTecCttoPlan', models.DateField(null=True)),
                ('FechIniLictCttoPlan', models.DateField(null=True)),
                ('FechLoaCttoPlan', models.DateField(null=True)),
                ('FechIniSerCttoPlan', models.DateField(null=True)),
                ('DuraCttoPlan', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('MHHCttoPlan', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('MontEstCttoPlan', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM01', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM02', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM03', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM04', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM05', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM06', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM07', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM08', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM09', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM10', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM11', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('FJM12', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('TipoCttoPlan', models.CharField(blank=True, max_length=20, null=True)),
                ('CoordTeccPlan', models.CharField(blank=True, max_length=20, null=True)),
                ('ReqSoleSCttoPlan', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
