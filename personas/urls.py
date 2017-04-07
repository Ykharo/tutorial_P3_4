from django.conf.urls import url
from personas.views import Personas,EditarContrato,CrearPersona,EditarPersona, ReportePersonasExcel, Bienvenida, DetallePersona,\
ModificarPersona,ReporteEDPExcel,ReporteODCExcel,ficha,DetalleEdp,ModificarEdp,BorrarEdp,ModificarOdc,BorrarOdc,ReporteFiniquito,\
crear_docODC
from . import models
from . import views

urlpatterns = [
    #url(r'^',include('seguridad.urls',namespace='seguridad')),
    url(r'^$',views.Bienvenida.as_view(), name="bienvenida"),
    url(r'^crear_persona/$',views.CrearPersona.as_view(), name="crear_persona"),
    url(r'^crear_persona/busqueda_ajax/$',views.BusquedaAjaxView.as_view(), name="Busqueda_ajax"),
    url(r'^crear_contratista/$',views.CrearContratista.as_view(), name="crear_contratista"),

    url(r'^personas/$',Personas.as_view(), name="personas"),
    url(r'^editar_contrato/(?P<id_ctto>[^/]+)$',views.EditarContrato, name="EditarContrato"),


    url(r'^ficha/$',ficha.as_view(), name="ficha"),
    #url(r'^detail/(?P<dni>[-\w]+)/$',views.EditarPersona.as_view(), name="editar_persona"),
    url(r'^detail/(?P<id_Persona>\d+)/$',views.EditarPersona.as_view(), name="editar_persona"),
    url(r'^reporte_personas_excel/$',ReportePersonasExcel.as_view(), name="reporte_personas_excel"),

    url(r'^reporte_edp_excel/$',ReporteEDPExcel.as_view(), name="reporte_edp_excel"),
    url(r'^reporte_odc_excel/$',ReporteODCExcel.as_view(), name="reporte_odc_excel"),

    url(r'^detalle_persona/(?P<pk>\d+)/$', DetallePersona.as_view(), name="detalle_persona"),
    url(r'^modificar_persona/(?P<pk>\d+)/$',ModificarPersona.as_view(), name="modificar_persona"),

    url(r'^crear_edp/(?P<id_ctto>\d+)/$',views.CrearEdp.as_view(), name="crear_edp"),
    url(r'^detalle_edp/(?P<pk>\d+)/$', DetalleEdp.as_view(), name="detalle_edp"),
    url(r'^modificar_edp/(?P<pk>\d+)/$',ModificarEdp.as_view(), name="modificar_edp"),
    url(r'^borrar_edp/(?P<pk>\d+)/$',BorrarEdp.as_view(), name="borrar_edp"),

    url(r'^crear_odc/(?P<id_ctto>\d+)/$',views.CrearOdc.as_view(), name="crear_odc"),
    url(r'^modificar_odc/(?P<pk>\d+)/$',ModificarOdc.as_view(), name="modificar_odc"),
    url(r'^borrar_odc/(?P<pk>\d+)/$',BorrarOdc.as_view(), name="borrar_odc"),
    url(r'^crear_docODC/(?P<id_odc>\d+)/$',views.crear_docODC.as_view(), name="crear_docODC"),

    url(r'^reporte_finiquito/(?P<id_ctto>\d+)/$',ReporteFiniquito.as_view(), name="reporte_finiquito"),



    url(r'^polls/$', views.upload, name='uplink'),
    url(r'^polls/import/', views.import_data, name="import"),
    url(r'^polls/import_EDP/', views.import_EDP_ODC, name="import_EDP_ODC"),
    url(r'^polls/export/(.*)', views.export_data, name="export"),
    url(r'^polls/import_sheet/', views.import_sheet, name="import_sheet"),
    url(r'^ctto/export/', views.export_r5, name="export_r5"),


    url(r'^prueba/',views.prueba, name="prueba"),

]
