from django import forms


class PaisForm(forms.Form):
    pais = forms.CharField()
    continente = forms.CharField()

