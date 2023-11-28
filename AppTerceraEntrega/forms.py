from django import forms


class PaisForm(forms.Form):
    pais = forms.CharField()
    continente = forms.CharField()

class BusquedaPaisForm(forms.Form):
    pais = forms.CharField()

<<<<<<< HEAD
class EquipoForm(forms.Form):
    equipo = forms.CharField()
    liga = forms.CharField()

class EstadioForm(forms.Form):
    estadio = forms.CharField()

=======
>>>>>>> a0e8d31d9f18fd347ffc70095e488d6848c4ed2e
