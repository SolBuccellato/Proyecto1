from django import forms




class DonacionesFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    celular = forms.IntegerField()

class AdopcionesFormulario(forms.Form):
    nombre = forms.CharField()
    mail = forms.CharField()


class RescatadosFormulario(forms.Form):
    nombre = forms.CharField()
    edad = forms.IntegerField()
    sexo = forms.CharField() 


