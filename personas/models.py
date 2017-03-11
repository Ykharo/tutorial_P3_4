# -*- encoding: utf-8 -*-
#encoding:utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models


class Area(models.Model):
    IdAreas = models.IntegerField(null=True, blank=True)
    NomArea = models.CharField(max_length=20)
    CodArea = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.NomArea



class Ceco(models.Model):
    IdCeco = models.IntegerField(null=True, blank=True)
    IdAreas = models.ForeignKey(Area)
    CodCeco = models.CharField(max_length=10, null=True, blank=True)
    NomCeco = models.CharField(max_length=100, null=True, blank=True)
    Budget = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)

    def __str__(self):
        return self.CodCeco


class Mdte(models.Model):
    IdMandante = models.IntegerField(null=True, blank=True)
    NomMandte = models.CharField(max_length=50)
    DirecMandte = models.CharField(max_length=100)
    RutMandte = models.CharField(max_length=20)

    def __str__(self):
        return self.NomMandte


class Ctta(models.Model):
    IdCtta = models.IntegerField(null=True, blank=True)
    NomCtta = models.CharField(max_length=100)
    DirCtta = models.CharField(max_length=100, null=True, blank=True)
    RutCtta = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.NomCtta

class Ctto(models.Model):
    LOCACION = (
        ("Local", "Local"),
        ("Nacional", "Nacional"),
        ("Extranjero", "Extranjero"),)


    IdCtto = models.IntegerField(null=True, blank=True)
    NumCtto = models.CharField(max_length=20, null=False)
    DescCtto = models.CharField(max_length=100, null=True, blank=True)
    MonedaCtto = models.CharField(max_length=5, null=True, blank=True)
    ValorCtto = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)
    IdCtta = models.ForeignKey(Ctta) # Agregar ForeignKey
    EstCtto = models.CharField(max_length=4, null=True, blank=True)
    FechIniCtto = models.DateField(null=False) #DateTimeField
    FechTerCtto = models.DateField(null=False)
    IdCecoCtto = models.ForeignKey(Ceco)
    CordCtto = models.CharField(max_length=100, null=True, blank=True)
    IdMandante = models.ForeignKey(Mdte)

    Carpeta = models.CharField(max_length=30, null=True, blank=True)
    TipoServ = models.CharField(max_length=25, null=True, blank=True)
    AjusteCom = models.DecimalField(decimal_places=2, max_digits=21, null=True, blank=True)
    AjustNumEDP = models.CharField( max_length=10, null=True, blank=True)
    AjustValEDP = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)
    AdjudicCtto = models.CharField( max_length=15, null=True, blank=True)
    LocalCtto = models.CharField( max_length=30,choices=LOCACION, default="Nacional",null=True, blank=True)
    TerrenCtto = models.CharField( max_length=10, null=True, blank=True)
    SeguroCtto = models.CharField( max_length=10, null=True, blank=True)

    FechSolCtto = models.DateField( null=True, blank=True)# Sept, Fecha Solicitud
    FechAppCtto = models.DateField( null=True, blank=True)# Sept, Fecha Aprob
    ObservCtto = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NumCtto

class Edp(models.Model):
    IdEDP = models.IntegerField( null=True, blank=True) # Agregar primary_key
    IdCtto = models.ForeignKey(Ctto) # Agregar ForeignKey
    NumEDP = models.CharField( max_length=10, null=False)
    ValEDP = models.DecimalField( decimal_places=2, max_digits=21,null=False)
    PeriodEDP = models.DateField( null=False)
    PeriodEDPTer = models.DateField( null=True, blank=True)# Sept, Final de Periodo
    DevAntEDP = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    RetEDP = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    DevRet = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    Estado = models.CharField( max_length=10)
    FactEDP = models.CharField( max_length=30, null=True, blank=True)

    PresenEDP = models.DateField( null=True, blank=True)# Sept, Fecha Present
    AprobEDP = models.DateField( null=True, blank=True)# Sept, Fecha Aprob
    ObservEDP = models.CharField(max_length=100, null=True, blank=True)

    PersLocal = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    PersNoLocal = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)

    PersHombres = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    PersMujeres = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)

    PersHHTotales = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    PersComVallenar = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    PersComFreirina = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    PersComHuasco = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    PersComAltoCarmen = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)

    #Ctto = relationship("Ctto")

    def __str__(self):
        return '%s %s' % (self.IdCtto.NumCtto, self.NumEDP)

class Odc(models.Model):
    IdODC = models.IntegerField(null=True, blank=True)# Agregar primary_key
    NumODC = models.CharField( max_length=8, null=False)
    IdCecoODC = models.ForeignKey(Ceco) # Agregar ForeignKey
    IdCtto =  models.ForeignKey( Ctto) #Agregar ForeignKey
    FechT_ODC = models.DateField( null=True, blank=True)
    ValorODC = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True) # Revisar, False y default=0
    DescripODC = models.CharField( max_length=50, null=True, blank=True)

    FechSolOdc = models.DateField( null=True, blank=True)# Sept, Fecha Solicitud
    FechAppOdc = models.DateField( null=True, blank=True)# Sept, Fecha Aprob
    ObservOdc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NumODC

class Monedas(models.Model):
    NomMoneda = models.CharField(max_length=4, null=False)
    ValorMoneda = models.DecimalField( decimal_places=2, max_digits=10,null=True, blank=True)
    FechMoneda = models.DateField( null=True, blank=True)

    def __str__(self):
        return self.NomMoneda




# _______________________________________________________

# Create your models here.
class Persona(models.Model):
    dni= models.CharField(primary_key=True,max_length=8)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)


#class Author(models.Model):
#    name = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.name


#class Category(models.Model):
#    name = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.name


#class Book(models.Model):
#    name = models.CharField('Book name', max_length=100)
#    author = models.ForeignKey(Author, blank=True, null=True)
#    author_email = models.EmailField('Author email', max_length=75, blank=True)
#    imported = models.BooleanField(default=False)
#    published = models.DateField('Published', blank=True, null=True)
#    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#    categories = models.ManyToManyField(Category, blank=True)

#    def __unicode__(self):
#        return self.name

# -------------------------------------------------------------

class Question(models.Model):
    STATUS = (
        ("Local", "Local"),
        ("Nacional", "Nacional"),
        ("Extranjero", "Extranjero"),)


    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    slug = models.CharField(max_length=10, unique=True,default="question")
    status = models.CharField(max_length=255,choices=STATUS)

    author = models.ForeignKey(User, related_name='author_assigned', null=True, blank=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    modificado_por = models.ForeignKey(User,related_name='modificador_assigned', null=True, blank=True)
    fecha_ultima_modificacion = models.DateTimeField(default=timezone.now)

#    def __str__(self):
#        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
