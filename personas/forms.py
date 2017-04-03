from django import forms

from .models import Persona, Ctto, Edp, Ctta, Odc

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
        fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','FechTerCtto',
        'IdCecoCtto','CordCtto','IdMandante','TipoServ','AjusteCom', 'AjustNumEDP','AjustValEDP','AdjudicCtto',
        'LocalCtto','TerrenCtto','SeguroCtto','FechSolCtto','FechAppCtto','ObservCtto']


        labels = {
            'FechIniCtto': 'Fecha de Inicio_1',
            'IdCecoCtto': 'Centro de Costo'
        }


        widgets = {
            'NumCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'DescCtto': forms.TextInput(attrs={'class': 'form-control','rows':2, 'cols':30}),
            #'MonedaCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'ValorCtto': forms.NumberInput(attrs={'class': 'form-control'} ),
            #'IdCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'EstCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'FechIniCtto': forms.DateInput(format='%m/%d/%Y'),
            'FechTerCtto': forms.DateInput(format='%m/%d/%Y'),
            #'IdCecoCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'CordCtto': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            #'IdMandante': forms.Textarea(attrs={'class': 'form-control'}),
            #'TipoServ': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),




        }



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
            #'IdCecoODC': forms.TextInput(attrs={'class': 'form-control'}),
            'FechT_ODC': forms.DateInput(format='%d/%m/%Y'),
            'ValorODC': forms.NumberInput(attrs={'class': 'form-control','localization': True}),
            'DescripODC': forms.TextInput(attrs={'class': 'form-control'}),

            'FechSolOdc': forms.DateInput(format='%d/%m/%Y'),
            'FechAppOdc': forms.DateInput(format='%d/%m/%Y'),
            'ObservEDP': forms.TextInput(attrs={'class': 'form-control'}),

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
        fields = ['NomCtta','DirCtta','RutCtta']
        labels = {
            'NomCtta': 'Nombre Contratista',
            'DirCtta': 'Dirección',
            'RutCtta': 'Rut'

        }

        widgets = {
            'NomCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'DirCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'RutCtta': forms.TextInput(attrs={'class': 'form-control'}),

                }
