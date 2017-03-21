from django import forms

from .models import Persona, Ctto, Edp, Ctta

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
        fields = ['IdCtto','NumEDP','ValEDP','PeriodEDP','PeriodEDPTer','DevAntEDP','RetEDP','DevRet','Estado','FactEDP'
                    ,'PresenEDP','AprobEDP','ObservEDP']
        labels = {
            'PeriodEDP': 'Periodo Inicio',
            'PeriodEDPTer': 'Periodo Término'
        }

        widgets = {
            #'IdCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'NumEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'ValEDP': forms.NumberInput(attrs={'class': 'form-control','localization': True}),

            'PeriodEDP': forms.DateInput(format='%d/%m/%Y'),
            'PeriodEDPTer': forms.DateInput(format='%d/%m/%Y'),
            'DevAntEDP': forms.TextInput(attrs={'class': 'form-control'}),
            'RetEDP': forms.NumberInput(attrs={'class': 'form-control'} ),
            'DevRet': forms.NumberInput(attrs={'class': 'form-control'} ),
            'Estado': forms.TextInput(attrs={'class': 'form-control'}),

            'FactEDP': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            'PresenEDP': forms.DateInput(format='%d/%m/%Y'),
            'AprobEDP': forms.DateInput(format='%d/%m/%Y'),
            'ObservEDP': forms.TextInput(attrs={'class': 'form-control'}),

                }

    def __init__(self, *args, **kwargs):
            try:
                valor = kwargs.pop('valor')
                super(EdpUpdateForm, self).__init__(*args, **kwargs)
                self.initial['IdCtto'] = valor
            except:
                    pass


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
