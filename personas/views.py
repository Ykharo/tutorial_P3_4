from django.shortcuts import render,redirect,get_object_or_404, render_to_response
#encoding:utf-8
# Create your views here.
from personas.models import Persona
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView


from django.conf import settings
from .forms import PersonaCreateForm, CttoUpdateForm, EdpUpdateForm, EdpCreateForm, CttaUpdateForm, OdcUpdateForm, OdcCreateForm

#Workbook nos permite crear libros en excel
from openpyxl import Workbook
#Nos devuelve un objeto resultado, en este caso un archivo de excel
from django.http.response import HttpResponse

from django.db.models import Avg, Max, Min, Count, Sum

from django.core.exceptions import ObjectDoesNotExist # para cuando exista moneda

from datetime import timedelta, datetime

import date_converter

#-------------------------------------------------------------------------

#from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from django import forms
from django.template import RequestContext
import django_excel as excel
from .models import Question, Choice, Area, Ceco, Mdte, Ctta, Ctto, Edp, Odc, Monedas

# No longer you need the following import statements if you use pyexcel >=0.2.2
import pyexcel.ext.xls
import pyexcel.ext.xlsx
import pyexcel.ext.ods3   # noqa


class UploadFileForm(forms.Form):
    file = forms.FileField()

# Create your views here.
def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render_to_response(
        'upload_form.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        },
        context_instance=RequestContext(request))

def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=0,
                model=Ceco,
                mapdict=['IdCeco', 'IdAreas', 'CodCeco', 'NomCeco', 'Budget'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render_to_response('upload_form.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def import_data(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def Ceco_func(row):
            q = Area.objects.filter(IdAreas=row[1])[0]
            row[1] = q
            return row
        def Ctto_func(row):
            print ('en Ctto')
            print (row)
            q1 = Ctta.objects.filter(IdCtta=row[5])[0]
            row[5] = q1
            q2 = Ceco.objects.filter(IdCeco=row[9])[0]
            row[9] = q2
            q3 = Mdte.objects.filter(IdMandante=row[11])[0]
            row[11] = q3
            return row
        def Edp_func(row):
            print ('en EDP')
            print (row)
            q4 = Ctto.objects.filter(IdCtto=row[1])[0]
            row[1] = q4
            return row
        def Odc_func(row):
            print(row)
            q5 = Ceco.objects.filter(IdCeco=row[2])[0]
            row[2] = q5
            q6 = Ctto.objects.filter(IdCtto=row[3])[0]
            row[3] = q6
            print('q5 y q6')
            print(q5,q6)
            return row

        if form.is_valid():
            request.FILES['file'].save_book_to_database(
                models=[Area, Ceco, Mdte, Ctta, Ctto, Edp, Odc],
                initializers=[None, Ceco_func, None, None,Ctto_func,Edp_func, Odc_func],
                mapdicts=[
                    ['IdAreas', 'NomArea', 'CodArea'],
                    ['IdCeco', 'IdAreas', 'CodCeco', 'NomCeco', 'Budget'],
                    ['IdMandante', 'NomMandte', 'DirecMandte', 'RutMandte'],
                    ['IdCtta', 'NomCtta', 'DirCtta', 'RutCtta'],
                    ['IdCtto', 'NumCtto', 'DescCtto', 'MonedaCtto', 'ValorCtto', 'IdCtta', 'EstCtto', 'FechIniCtto', 'FechTerCtto', 'IdCecoCtto', 'CordCtto', 'IdMandante',\
                    'Carpeta','TipoServ', 'AjusteCom','AjustNumEDP','AjustValEDP','AdjudicCtto','LocalCtto','TerrenCtto','SeguroCtto'],
                    ['IdEDP', 'IdCtto', 'NumEDP', 'ValEDP', 'PeriodEDP', 'DevAntEDP', 'RetEDP', 'DevRet', 'Estado', 'FactEDP'],
                    ['IdODC', 'NumODC', 'IdCecoODC', 'IdCtto', 'FechT_ODC', 'ValorODC', 'DescripODC']]

            )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def import_EDP_ODC(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        def Edp_func(row):
            print ('en EDP')
            print (row)
            q4 = Ctto.objects.filter(IdCtto=row[1])[0]
            row[1] = q4
            return row
        def Odc_func(row):
            print(row)
            q5 = Ceco.objects.filter(IdCeco=row[2])[0]
            row[2] = q5
            q6 = Ctto.objects.filter(IdCtto=row[3])[0]
            row[3] = q6
            print('q5 y q6')
            print(q5,q6)
            return row

        if form.is_valid():
            print('valido')
            request.FILES['file'].save_book_to_database(
                models=[Edp, Odc],
                initializers=[Edp_func, Odc_func],
                mapdicts=[
                    ['IdEDP', 'IdCtto', 'NumEDP', 'ValEDP', 'PeriodEDP', 'DevAntEDP', 'RetEDP', 'DevRet', 'Estado', 'FactEDP'],
                    ['IdODC', 'NumODC', 'IdCecoODC', 'IdCtto', 'FechT_ODC', 'ValorODC', 'DescripODC']]
            )
            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })
















def export_r5(request):
            column_names = ['IdCtto','NumCtto', 'DescCtto']
            exp_ctto = Ctto.objects.filter()



            e = Ctto.objects.filter()
            print(e)

            #q5 = Mdte.objects.filter(exp_ctto)
            #q6 = Ctto.objects.select_related().get(id=2)


            #print(q6.NomMandte)

            #exp_ctto = Ctto.objects.all()


            return excel.make_response_from_query_sets(
                exp_ctto,
                column_names,
                'xls',
                file_name="custom"
            )






def export_data(request, atype):
    if atype == "sheet":
        return excel.make_response_from_a_table(
            Question, 'xls', file_name="sheet")
    elif atype == "book":
        return excel.make_response_from_tables(
            [Question, Choice], 'xls', file_name="book")
    elif atype == "custom":
        question = Question.objects.get(slug='ide')
        query_sets = Choice.objects.filter(question=question)
        column_names = ['choice_text', 'id', 'votes']
        return excel.make_response_from_query_sets(
            query_sets,
            column_names,
            'xls',
            file_name="custom"
        )
    else:
        return HttpResponseBadRequest(
            "Bad request. please put one of these " +
            "in your url suffix: sheet, book or custom")










#-------------------------------------------------------------------------------






class ModificarPersona(UpdateView):
    #Especificamos que el modelo a utilizar va a ser Persona
    form_class = CttoUpdateForm

    model = Ctto
    #Establecemos que la plantilla se llamara modificar persona
    template_name = 'modificar_persona_new.html'
    #Determinamos los campos con los que se va a trabajar, esto es obligatorio sino nos saldra un error
    #fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','IdCecoCtto','CordCtto','IdMandante' ]
    #Con esta linea establecemos que se hara despues que la operacion de modificacion se complete correctamente
    success_url = reverse_lazy('personas:personas')



class DetallePersona(DetailView):
    model = Ctto
    template_name = 'detalle_persona_new.html'


#def sumarLista(lista):
#    sum=0
#    for i in range(0,len(lista)):
#        sum=sum+lista[i]
#    return sum



def prueba(request):
    CTTOS = Ctto.objects.all()
    ODC = Odc.objects.all()
    EDP = Edp.objects.all()



    #Aux = Ctto.objects.values_list('id','IdCtto','NumCtto')
    #Aux = Ctto.objects.get(id=3)
    #Aux2 = Aux.IdCtta.NomCtta

    #Aux = list(Odc.objects.filter(IdCtto__id='3').values_list('ValorODC',flat=True))
    Aux = Odc.objects.filter(IdCtto__id=3).aggregate(Sum('ValorODC'))

    #Aux2= Ctto.objects.filter(id=3)
    #Aux = sumarLista(Aux)
    #Aux2 = Aux[0]
    Aux2 =Aux['ValorODC__sum']

    print('Aux', Aux)
    print('Aux2', Aux2)
    html="<html><body> el valor es Aux : %s  Aux2 : </body></html>" % Aux, Aux2

    return HttpResponse(html)








#Nuestra clase hereda de la vista generica TemplateView

def fac(moneda):
    DolarProyecto=680
    valor = 0
    try:
        valor = Monedas.objects.get(NomMoneda=moneda).ValorMoneda
        valor = valor/DolarProyecto

    except ObjectDoesNotExist:
        valor =0

    return valor




class ReportePersonasExcel(TemplateView):

    #Usamos el metodo get para generar el archivo excel
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las personas de nuestra base de datos
        CTTOS = Ctto.objects.all()
        ODC = Odc.objects.all()
        EDP = Edp.objects.all()

        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'REPORTE DE PERSONAS'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['C3'] = 'Mandante'
        ws['D3'] = 'Tipo'
        ws['E3'] = 'N° Ctto.'
        ws['F3'] = 'Descripcion Servicio'
        ws['G3'] = 'Contratista'
        ws['H3'] = 'Carpeta'
        ws['I3'] = 'Fecha Ini Ctto'
        ws['J3'] = 'Fecha Term Ctto'
        ws['K3'] = 'Estatus'
        ws['L3'] = 'Centro de Costo'
        ws['M3'] = 'Cuenta'
        ws['N3'] = 'Descrip-Cuenta'
        ws['O3'] = 'Moneda Ctto'
        ws['P3'] = 'Valor Inicial'
        ws['Q3'] = 'Ajuste Commit Proyecto'
        ws['R3'] = 'EDP Ini Proy'
        ws['S3'] = 'EDP Ajust Proy'
        ws['T3'] = 'Adjudicación'
        ws['U3'] = 'Local'
        ws['V3'] = 'Terreno'
        ws['W3'] = 'Seguro'
        ws['X3'] = 'Valor ODC'
        ws['Y3'] = 'Valor EDP'
        ws['Z3'] = 'Val Actual Ctto'
        ws['AA3'] = 'Commitment Aprobado'
        ws['AB3'] = 'EDP Pagados Proy'
        ws['AC3'] = 'EDP Pagados Proy (USD)'
        ws['AD3'] = 'Commitment (USD)'
        ws['AE3'] = 'Commitment To Go (USD)'
        ws['AF3'] = 'Termino Actualizado'
        ws['AG3'] = 'Fecha Sol Ultima ODC'
        ws['AH3'] = 'Fecha Aprob Ultimo ODC'
        ws['AI3'] = 'Fecha Present Ultimo EDP'
        ws['AJ3'] = 'Fecha Aprob Ultimo EDP'
        ws['AK3'] = 'Fecha Periodo Ultimo EDP'
        ws['AL3'] = 'Fecha Solicitud Ctto'
        ws['AM3'] = 'Fecha Aprob Ctto'
        ws['AN3'] = 'Rut Ctta'
        ws['AO3'] = 'Observ Cttos'


        cont=4
        valcttoAct = 0
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for ctto in CTTOS:
            ws.cell(row=cont,column=3).value = ctto.IdMandante.NomMandte
            ws.cell(row=cont,column=4).value = ctto.TipoServ
            ws.cell(row=cont,column=5).value = ctto.NumCtto
            ws.cell(row=cont,column=6).value = ctto.DescCtto
            ws.cell(row=cont,column=7).value = ctto.IdCtta.NomCtta
            ws.cell(row=cont,column=8).value = ctto.Carpeta
            ws.cell(row=cont,column=9).value = ctto.FechIniCtto
            ws.cell(row=cont,column=10).value = ctto.FechTerCtto
            ws.cell(row=cont,column=11).value = ctto.EstCtto
            ws.cell(row=cont,column=12).value = ctto.IdCecoCtto.IdAreas.CodArea
            ws.cell(row=cont,column=13).value = ctto.IdCecoCtto.CodCeco
            ws.cell(row=cont,column=14).value = ctto.IdCecoCtto.NomCeco
            ws.cell(row=cont,column=15).value = ctto.MonedaCtto
            ws.cell(row=cont,column=16).value = ctto.ValorCtto
            ws.cell(row=cont,column=17).value = ctto.AjusteCom
            ws.cell(row=cont,column=18).value = ctto.AjustNumEDP
            ws.cell(row=cont,column=19).value = ctto.AjustValEDP
            ws.cell(row=cont,column=20).value = ctto.AdjudicCtto
            ws.cell(row=cont,column=21).value = ctto.LocalCtto
            ws.cell(row=cont,column=22).value = ctto.TerrenCtto
            ws.cell(row=cont,column=23).value = ctto.SeguroCtto

            factor = fac(ctto.MonedaCtto)
            sumaODC = Odc.objects.filter(IdCtto__id=ctto.id).aggregate(Sum('ValorODC'))['ValorODC__sum'] or 0
            sumaEDP = Edp.objects.filter(IdCtto__id=ctto.id).aggregate(Sum('ValEDP'))['ValEDP__sum'] or 0
            valcttoAct = ctto.ValorCtto + sumaODC
            commitment_ApProy =valcttoAct - ctto.AjusteCom
            auxiliar1 = ctto.ValorCtto
            auxiliar2 = ctto.AjusteCom
            edp_ApProy =sumaEDP - ctto.AjustValEDP
            commitment_togo =commitment_ApProy - edp_ApProy

            ws.cell(row=cont,column=24).value = sumaODC
            ws.cell(row=cont,column=25).value = sumaEDP
            ws.cell(row=cont,column=26).value = valcttoAct
            ws.cell(row=cont,column=27).value = commitment_ApProy
            ws.cell(row=cont,column=28).value = edp_ApProy
            ws.cell(row=cont,column=29).value = factor*edp_ApProy
            ws.cell(row=cont,column=30).value = factor*commitment_ApProy
            ws.cell(row=cont,column=31).value = factor*commitment_togo

            TerActualizado = (Odc.objects.filter(IdCtto__id=ctto.id).aggregate(Max('FechT_ODC'))['FechT_ODC__max']) or datetime(2009, 1, 1)
            #TerActualizado = datetime.strptime(TerActualizado, "%Y-%m-%d %H:%M:%S")


            if ctto.FechTerCtto.strftime('%F%H%M%S') > TerActualizado.strftime('%F%H%M%S'):
                TerActualizado = ctto.FechTerCtto

            ws.cell(row=cont,column=32).value = TerActualizado

            Fech_Sol_ultimaODC = (Odc.objects.filter(IdCtto__id=ctto.id).aggregate(Max('FechSolOdc'))['FechSolOdc__max']) or 0
            Fech_Apro_ultimaODC = (Odc.objects.filter(IdCtto__id=ctto.id).aggregate(Max('FechAppOdc'))['FechAppOdc__max']) or 0

            Fech_Pres_ultimaEDP = (Edp.objects.filter(IdCtto__id=ctto.id).aggregate(Max('PresenEDP'))['PresenEDP__max']) or 0
            Fech_Apro_ultimaEDP = (Edp.objects.filter(IdCtto__id=ctto.id).aggregate(Max('AprobEDP'))['AprobEDP__max']) or 0
            Fech_Period_ultimaEDP = (Edp.objects.filter(IdCtto__id=ctto.id).aggregate(Max('PeriodEDPTer'))['PeriodEDPTer__max']) or 0


            ws.cell(row=cont,column=33).value = Fech_Sol_ultimaODC
            ws.cell(row=cont,column=34).value = Fech_Apro_ultimaODC

            ws.cell(row=cont,column=35).value = Fech_Pres_ultimaEDP
            ws.cell(row=cont,column=36).value = Fech_Apro_ultimaEDP
            ws.cell(row=cont,column=37).value = Fech_Period_ultimaEDP

            ws.cell(row=cont,column=38).value = ctto.FechSolCtto
            ws.cell(row=cont,column=39).value = ctto.FechAppCtto
            ws.cell(row=cont,column=40).value = ctto.IdCtta.RutCtta

            ws.cell(row=cont,column=41).value = ctto.ObservCtto


            cont = cont + 1
        #Establecemos el nombre del archivo
        nombre_archivo ="ReportePersonasExcel.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        #response = HttpResponse(content_type="application/ms-excel")
        #contenido = "attachment; filename={0}".format(nombre_archivo)
        #response["Content-Disposition"] = contenido
        #wb.save(response)

        #['IdCtto', 'NumCtto', 'DescCtto', 'MonedaCtto', 'ValorCtto', 'IdCtta', 'EstCtto', 'FechIniCtto', 'FechTerCtto', 'IdCecoCtto', 'CordCtto', 'IdMandante',\
        #'Carpeta','TipoServ', 'AjusteCom','AjustNumEDP','AjustValEDP','AdjudicCtto','LocalCtto','TerrenCtto','SeguroCtto'],



        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=mydata.xlsx'

        wb.save(response)
        return response


class ReporteEDPExcel(TemplateView):

    #Usamos el metodo get para generar el archivo excel
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las personas de nuestra base de datos
        CTTOS = Ctto.objects.all()
        ODC = Odc.objects.all()
        EDP = Edp.objects.all()

        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'REPORTE DE EDP'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['B3'] = 'Ctto'
        ws['C3'] = 'Ctta'
        ws['D3'] = 'Descripción'
        ws['E3'] = 'Nº EDP'
        ws['F3'] = 'Moneda'

        ws['G3'] = 'Valor EDP'
        ws['H3'] = 'Dev Anticipo'
        ws['I3'] = 'Reten EDP'
        ws['J3'] = 'Dev Ret EDP'

        ws['K3'] = 'Valor EDP [USD]'


        ws['L3'] = 'P inicio'
        ws['M3'] = 'P Termino'
        ws['N3'] = 'Fecha Present EDP'
        ws['O3'] = 'Fecha Aprob EDP'
        ws['P3'] = 'Obs EDP'
        ws['Q3'] = 'EstCtto'

        cont=4
        valcttoAct = 0
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for ctto in CTTOS:
            factor = fac(ctto.MonedaCtto)
            for edp in Edp.objects.filter(IdCtto__id=ctto.id):

                ws.cell(row=cont,column=2).value = ctto.NumCtto
                ws.cell(row=cont,column=3).value = ctto.IdCtta.NomCtta
                ws.cell(row=cont,column=4).value = ctto.DescCtto
                ws.cell(row=cont,column=5).value = edp.NumEDP
                ws.cell(row=cont,column=6).value = ctto.MonedaCtto

                ws.cell(row=cont,column=7).value = edp.ValEDP
                ws.cell(row=cont,column=8).value = edp.DevAntEDP
                ws.cell(row=cont,column=9).value = edp.RetEDP
                ws.cell(row=cont,column=10).value = edp.DevRet

                ws.cell(row=cont,column=11).value = factor*edp.ValEDP

                ws.cell(row=cont,column=12).value = edp.PeriodEDP
                ws.cell(row=cont,column=13).value = edp.PeriodEDPTer
                ws.cell(row=cont,column=14).value = edp.PresenEDP
                ws.cell(row=cont,column=15).value = edp.AprobEDP
                ws.cell(row=cont,column=16).value = edp.ObservEDP
                ws.cell(row=cont,column=17).value = ctto.EstCtto

                cont = cont + 1

        #Establecemos el nombre del archivo
        nombre_archivo ="ReportePersonasExcel.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        #response = HttpResponse(content_type="application/ms-excel")
        #contenido = "attachment; filename={0}".format(nombre_archivo)
        #response["Content-Disposition"] = contenido
        #wb.save(response)

        #['IdCtto', 'NumCtto', 'DescCtto', 'MonedaCtto', 'ValorCtto', 'IdCtta', 'EstCtto', 'FechIniCtto', 'FechTerCtto', 'IdCecoCtto', 'CordCtto', 'IdMandante',\
        #'Carpeta','TipoServ', 'AjusteCom','AjustNumEDP','AjustValEDP','AdjudicCtto','LocalCtto','TerrenCtto','SeguroCtto'],



        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=mydata_Edp.xlsx'

        wb.save(response)
        return response




class ReporteODCExcel(TemplateView):

    #Usamos el metodo get para generar el archivo excel
    def get(self, request, *args, **kwargs):
        #Obtenemos todas las personas de nuestra base de datos
        CTTOS = Ctto.objects.all()
        ODC = Odc.objects.all()
        EDP = Edp.objects.all()

        #Creamos el libro de trabajo
        wb = Workbook()
        #Definimos como nuestra hoja de trabajo, la hoja activa, por defecto la primera del libro
        ws = wb.active
        #En la celda B1 ponemos el texto 'REPORTE DE PERSONAS'
        ws['B1'] = 'REPORTE DE ODC'
        #Juntamos las celdas desde la B1 hasta la E1, formando una sola celda
        ws.merge_cells('B1:E1')
        #Creamos los encabezados desde la celda B3 hasta la E3
        ws['B3'] = 'Ctto'
        ws['C3'] = 'Ctta'
        ws['D3'] = 'Descripción'
        ws['E3'] = 'Nº ODC'
        ws['F3'] = 'Valor ODC'
        ws['G3'] = 'Moneda'
        ws['H3'] = 'Valor ODC [USD]'
        ws['I3'] = 'Cuenta ODC'
        ws['J3'] = 'F Termino'
        ws['K3'] = 'Fecha Sol ODC'
        ws['L3'] = 'Fecha Aprob ODC'
        ws['M3'] = 'Obs ODC'
        ws['N3'] = 'EstCtto'

        cont=4
        valcttoAct = 0
        #Recorremos el conjunto de personas y vamos escribiendo cada uno de los datos en las celdas
        for ctto in CTTOS:
            factor = fac(ctto.MonedaCtto)
            for odc in Odc.objects.filter(IdCtto__id=ctto.id):

                ws.cell(row=cont,column=2).value = ctto.NumCtto
                ws.cell(row=cont,column=3).value = ctto.IdCtta.NomCtta
                ws.cell(row=cont,column=4).value = ctto.DescCtto
                ws.cell(row=cont,column=5).value = odc.NumODC
                ws.cell(row=cont,column=6).value = odc.ValorODC
                ws.cell(row=cont,column=7).value = ctto.MonedaCtto
                ws.cell(row=cont,column=8).value = factor*odc.ValorODC
                ws.cell(row=cont,column=9).value = odc.IdCecoODC.CodCeco
                ws.cell(row=cont,column=10).value = odc.FechT_ODC
                ws.cell(row=cont,column=11).value = odc.FechSolOdc
                ws.cell(row=cont,column=12).value = odc.FechAppOdc
                ws.cell(row=cont,column=13).value = odc.ObservOdc
                ws.cell(row=cont,column=14).value = ctto.EstCtto

                cont = cont + 1

        #Establecemos el nombre del archivo
        nombre_archivo ="ReportePersonasExcel.xlsx"
        #Definimos que el tipo de respuesta a devolver es un archivo de microsoft excel
        #response = HttpResponse(content_type="application/ms-excel")
        #contenido = "attachment; filename={0}".format(nombre_archivo)
        #response["Content-Disposition"] = contenido
        #wb.save(response)

        #['IdCtto', 'NumCtto', 'DescCtto', 'MonedaCtto', 'ValorCtto', 'IdCtta', 'EstCtto', 'FechIniCtto', 'FechTerCtto', 'IdCecoCtto', 'CordCtto', 'IdMandante',\
        #'Carpeta','TipoServ', 'AjusteCom','AjustNumEDP','AjustValEDP','AdjudicCtto','LocalCtto','TerrenCtto','SeguroCtto'],



        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=mydata_Odc.xlsx'

        wb.save(response)
        return response


class Bienvenida(TemplateView):
    #template_name = 'Tabla_Servicios.html'
    template_name = 'form.html'
# Create your views here.
class CrearPersona(CreateView):
    model = Ctto
    #fields =['dni','nombre','apellido_paterno','apellido_materno']
    template_name = 'crear_contrato_new.html'
    form_class = CttoUpdateForm
    success_url = reverse_lazy('personas:personas')

class Personas(ListView):
    model = Ctto
    template_name = 'personas_new.html'
    context_object_name = 'Cttos'
    buscar = "Contrato"

    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion primero del  context
        context = super(Personas, self).get_context_data(**kwargs)
        # Agregamos el publisher
        context['buscar'] = self.buscar
        return context

class EditarPersona(UpdateView):
    model = Persona

    #fields =['dni','nombre','apellido_paterno','apellido_materno']
    form_class = PersonaCreateForm
    template_model = 'crear_persona.html'
    #success_url = reverse_lazy('personas:personas')

    # def get(self,request,*arg,**kwargs):
    #    id_edit = request.GET['id']

class ficha(ListView):
    model = Ctto
    template_name = 'ficha.html'
    context_object_name = 'Cttos'



def EditarContrato(request,id_ctto):
    CTTO = Ctto.objects.all()
    ODC = Odc.objects.all()
    EDP = Edp.objects.all()

    valor = 0
    try:
        valor = Ctto.objects.get(NumCtto=id_ctto).id
        CTTO = Ctto.objects.get(NumCtto=id_ctto)
    except ObjectDoesNotExist:
        valor =0



    return render_to_response('editar_contratos_new.html',{'Ctto':CTTO,'Odc':ODC,'Edp':EDP,'id_ctto':valor })



class DetalleEdp(DetailView):
    model = Edp
    template_name = 'detalle_Edp_new.html'


# def sumarLista(lista):
#    sum=0
#    for i in range(0,len(lista)):
#        sum=sum+lista[i]
#    return sum

class ModificarEdp(UpdateView):
    #Especificamos que el modelo a utilizar va a ser Persona
    form_class = EdpUpdateForm

    model = Edp
    #Establecemos que la plantilla se llamara modificar persona
    template_name = 'modificar_edp_new.html'
    #Determinamos los campos con los que se va a trabajar, esto es obligatorio sino nos saldra un error
    #fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','IdCecoCtto','CordCtto','IdMandante' ]
    #Con esta linea establecemos que se hara despues que la operacion de modificacion se complete correctamente
    success_url = reverse_lazy('personas:personas')

    #def get_success_url(self):
        #Aux2 = Ctto.objects.get(id=self.kwargs['id_ctto']).NumCtto
        #print("Aux3")
        #print (edp.pk)
        #success_url = reverse('personas:EditarContrato',kwargs={'id_ctto': Aux2 })
        #success_url = reverse_lazy('personas:personas')


class CrearEdp(CreateView):
    model = Edp
    #fields =['dni','nombre','apellido_paterno','apellido_materno']
    template_name = 'crear_edp_new.html'
    form_class = EdpCreateForm
    success_url = reverse_lazy('personas:EditarContrato')
    D_edp = Edp


    def get_context_data(self, **kwargs):
        context = super(CrearEdp, self).get_context_data(**kwargs)
        context['Valedp'] = Edp.objects.all()
        context['Validctto'] = int(self.kwargs['id_ctto'])
        context['NumeroCtto'] = Ctto.objects.get(id=self.kwargs['id_ctto']).NumCtto
        context['DescripCtto'] = Ctto.objects.get(id=self.kwargs['id_ctto']).DescCtto

        print('valor de idctto =')
        print(self.kwargs['id_ctto'])
        return context

    def get_form_kwargs(self):
        kwargs = super(CrearEdp, self).get_form_kwargs()
        kwargs.update({'idctto':self.kwargs['id_ctto'],'dato_aux':'dato2'})

        return kwargs

    def get_success_url(self):
        Aux2 = Ctto.objects.get(id=self.kwargs['id_ctto']).NumCtto
        #print( Ctto.objects.get(id=int(self.kwargs['id_ctto']))).NumCtto
        return reverse('personas:EditarContrato',kwargs={'id_ctto': Aux2 })



class BorrarEdp(DeleteView):
    #Especificamos que el modelo a utilizar va a ser Persona
    form_class = EdpUpdateForm

    model = Edp
    #Establecemos que la plantilla se llamara modificar persona
    template_name = 'modificar_Edp_new.html'
    #Determinamos los campos con los que se va a trabajar, esto es obligatorio sino nos saldra un error
    #fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','IdCecoCtto','CordCtto','IdMandante' ]
    #Con esta linea establecemos que se hara despues que la operacion de modificacion se complete correctamente
    success_url = reverse_lazy('personas:personas')

    def get_context_data(self, **kwargs):
        context = super(BorrarEdp, self).get_context_data(**kwargs)

        context['NumeroCtto'] = Edp.objects.get(id=self.kwargs['pk']).IdCtto.NumCtto
        return context

    def get_success_url(self):
        Aux2 = Edp.objects.get(id=self.kwargs['pk']).IdCtto.NumCtto
        #print( Ctto.objects.get(id=int(self.kwargs['id_ctto']))).NumCtto
        return reverse('personas:EditarContrato',kwargs={'id_ctto': Aux2 })




class ModificarOdc(UpdateView):
    #Especificamos que el modelo a utilizar va a ser Persona
    form_class = OdcUpdateForm

    model = Odc
    #Establecemos que la plantilla se llamara modificar persona
    template_name = 'modificar_odc_new.html'
    #Determinamos los campos con los que se va a trabajar, esto es obligatorio sino nos saldra un error
    #fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','IdCecoCtto','CordCtto','IdMandante' ]
    #Con esta linea establecemos que se hara despues que la operacion de modificacion se complete correctamente
    success_url = reverse_lazy('personas:personas')

    #def get_success_url(self):
        #Aux2 = Ctto.objects.get(id=self.kwargs['id_ctto']).NumCtto
        #print("Aux3")
        #print (edp.pk)
        #success_url = reverse('personas:EditarContrato',kwargs={'id_ctto': Aux2 })
        #success_url = reverse_lazy('personas:personas')


class CrearOdc(CreateView):
    model = Odc
    #fields =['dni','nombre','apellido_paterno','apellido_materno']
    template_name = 'crear_odc_new.html'
    form_class = OdcCreateForm
    success_url = reverse_lazy('personas:EditarContrato')
    D_edp = Edp


    def get_context_data(self, **kwargs):
        context = super(CrearOdc, self).get_context_data(**kwargs)
        context['Valodc'] = Odc.objects.all()
        context['Validctto'] = int(self.kwargs['id_ctto'])
        context['NumeroCtto'] = Ctto.objects.get(id=self.kwargs['id_ctto']).NumCtto
        context['DescripCtto'] = Ctto.objects.get(id=self.kwargs['id_ctto']).DescCtto

        print('valor de idctto =')
        print(self.kwargs['id_ctto'])
        return context

    def get_form_kwargs(self):
        kwargs = super(CrearOdc, self).get_form_kwargs()
        kwargs.update({'idctto':self.kwargs['id_ctto'],'dato_aux':'dato2'})

        return kwargs

    def get_success_url(self):
        Aux2 = Ctto.objects.get(id=self.kwargs['id_ctto']).NumCtto
        #print( Ctto.objects.get(id=int(self.kwargs['id_ctto']))).NumCtto
        return reverse('personas:EditarContrato',kwargs={'id_ctto': Aux2 })



class BorrarOdc(DeleteView):
    #Especificamos que el modelo a utilizar va a ser Persona
    form_class = OdcUpdateForm

    model = Odc
    #Establecemos que la plantilla se llamara modificar persona
    template_name = 'modificar_Odc_new.html'
    #Determinamos los campos con los que se va a trabajar, esto es obligatorio sino nos saldra un error
    #fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','IdCecoCtto','CordCtto','IdMandante' ]
    #Con esta linea establecemos que se hara despues que la operacion de modificacion se complete correctamente
    success_url = reverse_lazy('personas:personas')







from django.core import serializers


class BusquedaAjaxView(TemplateView):

    def get(self, request, *arg, **kwargs):
        id_ceco =request.GET['idajx']
        nombre_ceco = Ceco.objects.filter(id=id_ceco)
        data = serializers.serialize('json',nombre_ceco,
                    fields=('NomCeco'))
        return HttpResponse(data, content_type ='application/json')

class CrearContratista(CreateView):
        model = Ctta
        #fields =['dni','nombre','apellido_paterno','apellido_materno']
        template_name = 'crear_ctta_new.html'
        form_class = CttaUpdateForm
        success_url = reverse_lazy('personas:crear_persona')
