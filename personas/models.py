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


class PersonalProyecto(models.Model):
    Nombre = models.CharField(max_length=100, null=True, blank=True)
    Cargo = models.CharField(max_length=50, null=True, blank=True)
    Correo = models.CharField(max_length=50, null=True, blank=True)
    IdArea = models.ForeignKey(Area)
    Cel = models.CharField(max_length=20, null=True, blank=True)
    CI = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '%s' % (self.Nombre)




class Duenoceco(models.Model):

    DOCIDENTIDAD = (
        ("CI", "CI"),
        ("Pasaporte", "Pasaporte"),)

    NomDueno = models.CharField(max_length=20)
    DocIdDueno = models.CharField(max_length=10,choices=DOCIDENTIDAD, default="CI", null=True, blank=True)
    NumDocDueno = models.CharField(max_length=15, null=True, blank=True)
    CargoDueno = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.NomDueno



class Ceco(models.Model):
    IdCeco = models.IntegerField(null=True, blank=True)
    IdAreas = models.ForeignKey(Area)
    CodCeco = models.CharField(max_length=10, null=True, blank=True)
    NomCeco = models.CharField(max_length=100, null=True, blank=True)
    IdDueno = models.ForeignKey(Duenoceco)
    Budget = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)


    class Meta:
        ordering = ['CodCeco']


    def __str__(self):
        return '%s %s' % (self.CodCeco, self.NomCeco)

class Mdte(models.Model):
    IdMandante = models.IntegerField(null=True, blank=True)
    NomMandte = models.CharField(max_length=50)
    RutMandte = models.CharField(max_length=20)
    DirecMandte = models.CharField(max_length=100)
    ComunaMandte = models.CharField(max_length=50,null=True, blank=True)
    CiudadMandte = models.CharField(max_length=50,null=True, blank=True)
    NotarioMandte = models.CharField(max_length=100,null=True, blank=True)
    FechDocpersonMandte = models.DateField(null=True, blank=True)
    NotariapersonMandte = models.CharField(max_length=100,null=True, blank=True)


    def __str__(self):
        return self.NomMandte


class Ctta(models.Model):
    IdCtta = models.IntegerField(null=True, blank=True)

    RutCtta = models.CharField(max_length=15, null=True, blank=True)
    NomCtta = models.CharField(max_length=100)
    DirCtta = models.CharField(max_length=100, null=True, blank=True)
    ComunaCtta = models.CharField(max_length=50,null=True, blank=True)
    CiudadCtta = models.CharField(max_length=50,null=True, blank=True)
    GiroCtta = models.CharField(max_length=50,null=True, blank=True)
    BcoCtta = models.CharField(max_length=50,null=True, blank=True)
    NumCtaCtta = models.CharField(max_length=50,null=True, blank=True)


    Rep1Ctta = models.CharField(max_length=100, null=True, blank=True)
    RutRep1Ctta = models.CharField(max_length=100, null=True, blank=True)
    Rep2Ctta = models.CharField(max_length=100, null=True, blank=True)
    RutRep2Ctta = models.CharField(max_length=100, null=True, blank=True)

    NotarioCtta = models.CharField(max_length=100,null=True, blank=True)
    FechDocpersonCtta = models.DateField(null=True, blank=True)
    NotariapersonCtta = models.CharField(max_length=100,null=True, blank=True)

    class Meta:
        ordering = ['NomCtta']

    def __str__(self):
        return self.NomCtta


class PersonalCtta(models.Model):
    Nombre = models.CharField(max_length=100, null=True, blank=True)
    Cargo = models.CharField(max_length=50, null=True, blank=True)
    Correo = models.CharField(max_length=50, null=True, blank=True)
    IdCtta = models.ForeignKey(Ctta)
    Cel = models.CharField(max_length=20, null=True, blank=True)
    CI = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ['IdCtta']


    def __str__(self):
        return '%s - %s' % (self.IdCtta.NomCtta, self.Nombre)




class Ctto(models.Model):
    LOCACION = (
        ("Local", "Local"),
        ("Nacional", "Nacional"),
        ("Extranjero", "Extranjero"),)

    TIPOSERV = (
        ("Contrato", "Contrato"),
        ("Orden de Servicio", "Orden de Servicio"),
        ("Convenio", "Convenio"),("Orden de Compra", "Orden de Compra"))

    MONEDA = (
        ("CLP", "CLP"),
        ("USD", "USD"),
        ("UF", "UF"),("EUR", "EUR"),("CAD", "CAD"))

    ADJUDICACION = (
        ("Directa", "Directa"),
        ("Cotizaciones", "Cotizaciones"),
        ("Licitación", "Licitación"))

    TERRENOCONTRATO = (
        ( "Si","Con Terreno"),
        ( "No","Sin Terreno"))

    SEGURO = (
        ("Si","Aplica Seguro"),
        ("No","No Aplica Seguro"))

    IMPUESTO = (
        ("IVA","Afecto a IVA"),
        ("NO_IVA","No Afecto a IVA"),
        ("RET_Legal","Retención Legal"))

    PROVISION = (
        ("Calculada","Calculada"),
        ("Informada","Informada"))


    IdCtto = models.IntegerField(null=True, blank=True)
    NumCtto = models.CharField(max_length=20, null=False)
    DescCtto = models.CharField(max_length=100, null=True, blank=True)
    AlcanceCtto = models.CharField(max_length=200, null=True, blank=True)
    MonedaCtto = models.CharField(max_length=5, choices=MONEDA, default="CLP",null=True, blank=True)
    ValorCtto = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)
    IdCtta = models.ForeignKey(Ctta) # Agregar ForeignKey
    EstCtto = models.CharField(max_length=4, null=True, blank=True)
    FechIniCtto = models.DateField(null=False) #DateTimeField
    FechTerCtto = models.DateField(null=False)
    IdCecoCtto = models.ForeignKey(Ceco)

    CordCtto = models.ForeignKey(PersonalProyecto,default="1")
    AdminCttoCtta = models.ForeignKey(PersonalCtta,default="1")

    IdMandante = models.ForeignKey(Mdte)


    Carpeta = models.CharField(max_length=30, null=True, blank=True)
    TipoServ = models.CharField(max_length=25, choices=TIPOSERV, default="Contrato",null=True, blank=True)
    AjusteCom = models.DecimalField(decimal_places=2,default= 0, max_digits=21, null=True, blank=True)
    AjustNumEDP = models.CharField( max_length=10,default= "1",null=True, blank=True)
    AjustValEDP = models.DecimalField(decimal_places=2,default= 0,max_digits=21,null=True, blank=True)
    AdjudicCtto = models.CharField( max_length=15, choices=ADJUDICACION, default="Directa", null=True, blank=True)
    LocalCtto = models.CharField( max_length=30,choices=LOCACION, default="Nacional",null=True, blank=True)
    TerrenCtto = models.CharField( max_length=10,choices=TERRENOCONTRATO, default="No", null=True, blank=True)
    SeguroCtto = models.CharField( max_length=10,choices=SEGURO, default="No", null=True, blank=True)
    LugarCtto = models.CharField( max_length=50, null=True, blank=True)

    ProvisCtto = models.CharField( max_length=10,choices=PROVISION , default="Calculada", null=True, blank=True)

    FechSolCtto = models.DateField( null=True, blank=True)# Sept, Fecha Solicitud
    FechAppCtto = models.DateField( null=True, blank=True)# Sept, Fecha Aprob
    ObservCtto = models.CharField(max_length=100, null=True, blank=True)

    DocOferta = models.CharField(max_length=100, null=True, blank=True)
    FechOferta = models.DateField(null=True, blank=True)
    FechCartaAdj = models.DateField(null=True, blank=True)
    IvaOferta = models.CharField(max_length=30, choices=IMPUESTO, default="IVA",null=True, blank=True)
    Anticipo = models.DecimalField(decimal_places=2, max_digits=21, null=True, blank=True)
    Modalidad = models.CharField(max_length=50, null=True, blank=True)

    Boleta = models.DecimalField(decimal_places=2, max_digits=21, null=True, blank=True)
    MonedaBoleta = models.CharField(max_length=5, choices=MONEDA, default="CLP",null=True, blank=True)
    VigenBoleta = models.CharField(max_length=100, null=True, blank=True)
    FechVigenBoleta = models.DateField( null=True, blank=True)
    RetenCtto = models.CharField(max_length=100, null=True, blank=True)



    def __str__(self):
        return self.NumCtto


class Edp(models.Model):
    IdEDP = models.IntegerField( null=True, blank=True) # Agregar primary_key
    IdCtto = models.ForeignKey(Ctto) # Agregar ForeignKey
    NumEDP = models.CharField( max_length=10, null=False)
    ValEDP = models.DecimalField( decimal_places=2, max_digits=21,null=False)
    PeriodEDP = models.DateField( null=False)
    PeriodEDPTer = models.DateField( null=True, blank=True)# Sept, Final de Periodo

    AnticipoEDP = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    DevAntEDP = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    RetEDP = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    DevRet = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    DescuentoEDP = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)

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

class ItemOdc(models.Model):
    NumItem = models.CharField( max_length=8, null=False)
    IdCecoODC = models.ForeignKey(Ceco) # Agregar ForeignKey
    IdODC =  models.ForeignKey( Odc) #Agregar ForeignKey
    DescripItem = models.CharField( max_length=50, null=True, blank=True)
    UnidItem = models.CharField( max_length=50, null=True, blank=True)
    CantItem = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True) # Revisar, False y default=0
    PuItem = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    TotalItem = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)
    ObservItem = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NumItem

    def save(self):
        self.TotalItem = self.CantItem * self.PuItem
        super(ItemOdc, self).save()

class ItemCtto(models.Model):
    NumItem = models.CharField( max_length=8, null=False)
    IdCecoCtto = models.ForeignKey(Ceco) # Agregar ForeignKey
    IdCtto =  models.ForeignKey( Ctto) #Agregar ForeignKey
    DescripItem = models.CharField( max_length=50, null=True, blank=True)
    UnidItem = models.CharField( max_length=50, null=True, blank=True)
    CantItem = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True) # Revisar, False y default=0
    PuItem = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    TotalItem = models.DecimalField(decimal_places=2, max_digits=21,null=True, blank=True)
    ObservItem = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NumItem

    def save(self):
        self.TotalItem = self.CantItem * self.PuItem
        super(ItemCtto, self).save()

class AportesCtto(models.Model):
    NumItem = models.CharField( max_length=8, null=False)
    IdCtto =  models.ForeignKey( Ctto) #Agregar ForeignKey
    Aporte = models.CharField( max_length=100, null=True, blank=True)
    ObsAporte = models.CharField( max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NumItem

class MultasPerClaveCtto(models.Model):

    MONEDA = (
        ("CLP", "CLP"),
        ("USD", "USD"),
        ("UF", "UF"),("EUR", "EUR"),("CAD", "CAD"))

    NumItem = models.CharField( max_length=8, null=False)
    IdCtto =  models.ForeignKey( Ctto) #Agregar ForeignKey
    NomPersClave = models.CharField( max_length=50, null=True, blank=True)
    CargPersClave = models.CharField( max_length=50, null=True, blank=True)
    Multa = models.DecimalField( decimal_places=2, max_digits=21,null=True, blank=True)
    Moneda = models.CharField(max_length=5, choices=MONEDA, default="UF",null=True, blank=True)
    ObsMulta = models.CharField( max_length=100, null=True, blank=True)

    def __str__(self):
        return self.NumItem






class Reprentantes(models.Model):
    IdDuenoCeco = models.ForeignKey(Ceco)
    IdMandante = models.ForeignKey(Mdte)

    def __str__(self):
        return '%s %s' % (self.IdDuenoCeco, self.IdMandante)





class CoordCtto(models.Model):
    IdPersCtta = models.ForeignKey(PersonalCtta)
    IdCtto = models.ForeignKey(Ctto)
    IdPersProy = models.ForeignKey(PersonalProyecto)

    def __str__(self):
        return '%s %s' % (self.IdCtto, self.IdPersCtta)








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
