from django import forms
from django.forms import inlineformset_factory

from .models import Persona, Ctto, Edp, Ctta, Odc, ItemOdc, ItemCtto, Ceco, AportesCtto, MultasPerClaveCtto,PersonalProyecto,PersonalCtta

class PersonaCreateForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('dni','nombre','apellido_paterno','apellido_materno')
        labels = {
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.Textarea(attrs={'class': 'form-control'}),

        }

class CttoUpdateForm(forms.ModelForm):

    class Meta:
        model = Ctto
        fields = ['NumCtto','DescCtto','AlcanceCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','FechTerCtto',
        'IdCecoCtto','CordCtto','IdMandante','TipoServ','AjusteCom', 'AjustNumEDP','AjustValEDP','AdjudicCtto',
        'LocalCtto','TerrenCtto','SeguroCtto','FechSolCtto','FechAppCtto','ObservCtto','LugarCtto','DocOferta','FechOferta','FechCartaAdj',
        'IvaOferta', 'Anticipo', 'Modalidad', 'Boleta', 'MonedaBoleta', 'FechVigenBoleta', 'RetenCtto','AdminCttoCtta','ProvisCtto'

        ]


        labels = {
            'FechIniCtto': 'Fecha de Inicio',
            'FechTerCtto': 'Fecha de Término',
            'IdCecoCtto': 'Centro de Costo',
            'CordCtto': 'Coord Téc NU',
            'AdminCttoCtta': 'Admin Ctta',
            'Tipo Prov': 'ProvisCtto'
        }


        widgets = {
            'NumCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'DescCtto': forms.TextInput(attrs={'class': 'form-control','rows':2, 'cols':30}),
            'AlcanceCtto': forms.Textarea(attrs={'class': 'form-control'}),
            #'MonedaCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'ValorCtto': forms.NumberInput(attrs={'class': 'form-control'} ),
            #'IdCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'EstCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'FechIniCtto': forms.DateInput(format='%d/%m/%Y'),
            'FechTerCtto': forms.DateInput(format='%d/%m/%Y'),
            #'IdCecoCtto': forms.TextInput(attrs={'class': 'form-control'}),
            #'CordCtto': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            #'IdMandante': forms.Textarea(attrs={'class': 'form-control'}),
            #'TipoServ': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            'Modalidad': forms.TextInput(attrs={'class': 'form-control','rows':2, 'cols':30}),
            'DocOferta': forms.TextInput(attrs={'class': 'form-control','rows':2, 'cols':20}),
            'LugarCtto': forms.TextInput(attrs={'class': 'form-control','rows':2, 'cols':30}),
            'ObservCtto': forms.TextInput(attrs={'class': 'form-control','rows':2, 'cols':30}),
            'FechVigenBoleta': forms.DateInput(format='%d/%m/%Y')
        }
    def __init__(self, *args, **kwargs):
        super(CttoUpdateForm, self).__init__(*args, **kwargs)
        self.fields['IdCtta'].widget.attrs['style'] = "width:550px"
        self.fields['IdCecoCtto'].widget.attrs['style'] = "width:550px"
        self.fields['AdminCttoCtta'].widget.attrs['style'] = "width:550px"


class EdpUpdateForm(forms.ModelForm):

    class Meta:
        model = Edp
        fields = ['IdCtto','NumEDP','ValEDP','PeriodEDP','PeriodEDPTer','AnticipoEDP','DevAntEDP','RetEDP','DevRet','DescuentoEDP','Estado','FactEDP'
                    ,'PresenEDP','AprobEDP','ObservEDP']
        labels = {
            'PeriodEDP': 'Periodo Inicio',
            'PeriodEDPTer': 'Periodo Término',
            'AnticipoEDP': 'Anticipo',
            'DescuentoEDP': 'Descuento'
        }

        widgets = {
            #'IdCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'NumEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'ValEDP': forms.NumberInput(attrs={'class': 'form-control','localization': True}),

            'PeriodEDP': forms.DateInput(format='%d/%m/%Y'),
            'PeriodEDPTer': forms.DateInput(format='%d/%m/%Y'),

            'AnticipoEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'DevAntEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'RetEDP': forms.NumberInput(attrs={'class': 'form-control'} ),
            'DevRet': forms.NumberInput(attrs={'class': 'form-control'} ),
            'DescuentoEDP': forms.TextInput(attrs={'class': 'form-control'}),


            'Estado': forms.TextInput(attrs={'class': 'form-control'}),
            'FactEDP': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            'PresenEDP': forms.DateInput(format='%d/%m/%Y'),
            'AprobEDP': forms.DateInput(format='%d/%m/%Y'),
            'ObservEDP': forms.TextInput(attrs={'class': 'form-control'}),

                }


class EdpCreateForm(forms.ModelForm):

    class Meta:
        model = Edp
        fields = ['IdCtto','NumEDP','ValEDP','PeriodEDP','PeriodEDPTer','AnticipoEDP','DevAntEDP','RetEDP','DevRet','DescuentoEDP','Estado','FactEDP'
                    ,'PresenEDP','AprobEDP','ObservEDP']
        labels = {
            'PeriodEDP': 'Periodo Inicio',
            'PeriodEDPTer': 'Periodo Término',
            'AnticipoEDP': 'Anticipo',
            'DescuentoEDP': 'Descuento'
        }

        widgets = {
            #'IdCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'NumEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'ValEDP': forms.NumberInput(attrs={'class': 'form-control','localization': True}),

            'PeriodEDP': forms.DateInput(format='%d/%m/%Y'),
            'PeriodEDPTer': forms.DateInput(format='%d/%m/%Y'),

            'AnticipoEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'DevAntEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'RetEDP': forms.NumberInput(attrs={'class': 'form-control'} ),
            'DevRet': forms.NumberInput(attrs={'class': 'form-control'} ),
            'DescuentoEDP': forms.TextInput(attrs={'class': 'form-control'}),

            'Estado': forms.TextInput(attrs={'class': 'form-control'}),
            'FactEDP': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            'PresenEDP': forms.DateInput(format='%d/%m/%Y'),
            'AprobEDP': forms.DateInput(format='%d/%m/%Y'),
            'ObservEDP': forms.TextInput(attrs={'class': 'form-control'}),

                }

    def __init__(self, *args, **kwargs):
                valor1 = kwargs.pop('idctto')
                valor2 = kwargs.pop('dato_aux')
                super(EdpCreateForm, self).__init__(*args, **kwargs)
                self.initial['IdCtto'] = valor1
                self.initial['valor2'] = valor2




class OdcUpdateForm(forms.ModelForm):

    class Meta:
        model = Odc
        fields = ['IdCtto','NumODC','IdCecoODC','FechT_ODC','ValorODC','DescripODC','FechSolOdc','FechAppOdc','ObservOdc']
        labels = {
            'IdCecoODC': 'Cuenta Contable',
            'FechT_ODC': 'Fecha de Término'
        }

        widgets = {
            #'IdCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'NumODC': forms.TextInput(attrs={'class': 'form-control'}),
            #'IdCecoODC': forms.TextInput(attrs={'class': 'form-control'}),
            'FechT_ODC': forms.DateInput(format='%d/%m/%Y'),
            'ValorODC': forms.NumberInput(attrs={'class': 'form-control','localization': True}),
            'DescripODC': forms.TextInput(attrs={'class': 'form-control'}),

            'FechSolOdc': forms.DateInput(format='%d/%m/%Y'),
            'FechAppOdc': forms.DateInput(format='%d/%m/%Y'),
            'ObservEDP': forms.TextInput(attrs={'class': 'form-control'}),

                }



class OdcCreateForm(forms.ModelForm):

    class Meta:
        model = Odc

        fields = ['IdCtto','NumODC','IdCecoODC','FechT_ODC','ValorODC','DescripODC','FechSolOdc','FechAppOdc','ObservOdc']
        labels = {
            'IdCecoODC': 'Cuenta Contable',
            'FechT_ODC': 'Fecha de Término'
        }

        widgets = {
            #'IdCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'NumODC': forms.TextInput(attrs={'class': 'form-control'}),
            #'IdCecoODC': forms.ModelChoiceField(queryset=Ceco.objects.all),
            'FechT_ODC': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'ValorODC': forms.NumberInput(attrs={'class': 'form-control','localization': True}),
            'DescripODC': forms.TextInput(attrs={'class': 'form-control'}),

            'FechSolOdc': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'FechAppOdc': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control'}),
            'ObservOdc': forms.TextInput(attrs={'class': 'form-control'}),

                }

    def __init__(self, *args, **kwargs):
                valor1 = kwargs.pop('idctto')
                valor2 = kwargs.pop('dato_aux')
                super(OdcCreateForm, self).__init__(*args, **kwargs)
                self.initial['IdCtto'] = valor1
                self.initial['valor2'] = valor2






class CttaUpdateForm(forms.ModelForm):

    class Meta:
        model = Ctta
        exclude = ()
        fields = ['NomCtta','RutCtta','DirCtta','ComunaCtta','CiudadCtta','GiroCtta']
        labels = {
            'NomCtta': 'Nombre Contratista',
            'DirCtta': 'Dirección',
            'RutCtta': 'Rut'

        }

        widgets = {
            'NomCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'RutCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'DirCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'ComunaCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'CiudadCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'GiroCtta': forms.TextInput(attrs={'class': 'form-control'}),
                }









class ItemOdcForm(forms.ModelForm):
    class Meta:
        model = ItemOdc
        exclude = ('ObservItem',)
        labels = {
            'NumItem': 'Item',
            'IdCecoODC': 'Cuenta',
            'DescripItem': 'Descripción',
            'UnidItem': 'Unidad',
            'CantItem': 'Cantidad',
            'PuItem': 'Precio Unitario',
            'TotalItem': 'Total',
            'ObservItem': 'Obs'
        }



    def __init__(self, *args, **kwargs):
        super(ItemOdcForm, self).__init__(*args, **kwargs)
        self.fields['NumItem'].widget.attrs['style'] = "width:150px"
        self.fields['IdCecoODC'].widget.attrs['style'] = "width:300px"
        self.fields['DescripItem'].widget.attrs['style'] = "width:800px"



ItemOdcFormSet = inlineformset_factory(Odc, ItemOdc,
                                            form=ItemOdcForm, extra=1)



class ItemCttoForm(forms.ModelForm):
    class Meta:
        model = ItemCtto
        exclude = ()
        labels = {
            'NumItem': 'Item',
            'IdCecoCtto': 'Cuenta',
            'DescripItem': 'Descripción',
            'UnidItem': 'Unidad',
            'CantItem': 'Cantidad',
            'PuItem': 'Precio Unitario',
            'TotalItem': 'Total',
            'ObservItem': 'Obs'
        }

        widgets = {
            'NumItem': forms.TextInput(attrs={'class': 'form-control','maxlength':5}),
            'DescripItem': forms.TextInput(attrs={'class': 'form-control','maxlength':50}),

                }

ItemCttoFormSet = inlineformset_factory(Ctto, ItemCtto,form=ItemCttoForm, extra=1)



class AportesCttoForm(forms.ModelForm):
    class Meta:
        model = AportesCtto
        exclude = ()
        labels = {
            'NumItem': 'Item',
            'Aporte': 'Descripción',
            'ObsAporte': 'Obs'
        }

        widgets = {
            'NumItem': forms.TextInput(attrs={'class': 'form-control','maxlength':5}),
            'ObsAporte': forms.TextInput(attrs={'class': 'form-control','maxlength':50}),

                }

AportesCttoFormSet = inlineformset_factory(Ctto, AportesCtto,form=AportesCttoForm, extra=1)

class MultasPerClaveCttoForm(forms.ModelForm):
    class Meta:
        model = MultasPerClaveCtto
        exclude = ()
        labels = {
            'NumItem': 'Item',
            'NomPersClave': 'Nombre Pers.Clave',
            'CargPersClave': 'Cargo Pers.Clave',
            'Multa': 'Multa',
            'Moneda': 'Moneda',
            'ObsMulta': 'Obs'

        }

        widgets = {
            'NumItem': forms.TextInput(attrs={'class': 'form-control','maxlength':5}),
            'ObsMulta': forms.TextInput(attrs={'class': 'form-control','maxlength':50}),

                }

MultasPerClaveCttoFormSet = inlineformset_factory(Ctto, MultasPerClaveCtto,form=MultasPerClaveCttoForm, extra=1)




class PersonalProyUpdateForm(forms.ModelForm):

    class Meta:
        model = PersonalProyecto
        exclude = ()
        fields = ['Nombre','Cargo','Correo','IdArea','Cel','CI']
        labels = {

        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control'}),
            'Cel': forms.TextInput(attrs={'class': 'form-control'}),
            'CI': forms.TextInput(attrs={'class': 'form-control'}),


                }




class PersonalCttaUpdateForm(forms.ModelForm):

    class Meta:
        model = PersonalCtta
        exclude = ()
        fields = ['Nombre','Cargo','Correo','IdCtta','Cel','CI']
        labels = {

        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control'}),
            'Cel': forms.TextInput(attrs={'class': 'form-control'}),
            'CI': forms.TextInput(attrs={'class': 'form-control'}),


                }
