from django import forms


class PaisForm(forms.Form):
    pais = forms.CharField()
    continente = forms.CharField()

class BusquedaPaisForm(forms.Form):
    pais = forms.CharField()

class EquipoForm(forms.Form):
    equipo = forms.CharField()
    liga = forms.CharField()

class EstadioForm(forms.Form):
    estadio = forms.CharField()

