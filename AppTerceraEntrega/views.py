from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppTerceraEntrega.models import Pais, Equipo, Estadio
from AppTerceraEntrega.forms import PaisForm, BusquedaPaisForm, EquipoForm, EstadioForm


def mostrar_paises(request):
    paises = Pais.objects.all()
    contexto = {
        "paises": paises,
        "form": BusquedaPaisForm()
    }
    return render(request, "AppTerceraEntrega/paises.html", contexto)

def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {
        "equipos": equipos,
        "form": BusquedaPaisForm()
    }
    return render(request, "AppTerceraEntrega/equipos.html", contexto)

def mostrar_estadios(request):
    estadios = Estadio.objects.all()
    contexto = {
        "estadios": estadios,
        "form": BusquedaPaisForm()
    }
    return render(request, "AppTerceraEntrega/estadios.html", contexto)


# Create your views here.
def crear_pais(request):
    pais = Pais(pais="España", continente="Europa")
    pais.save()

    return redirect("/app/crear_pais")  # get

def crear_pais_form(request):

    if request.method == "POST":
        pais_formulario = PaisForm(request.POST)
        if pais_formulario.is_valid():
            informacion = pais_formulario.cleaned_data
            pais_crear = Pais(pais=informacion["pais"], continente=informacion["continente"])
            pais_crear.save()
            return redirect("/app/paises/")

    pais_formulario = PaisForm()
    contexto = {
        "form": pais_formulario
    }
    return render(request, "AppTerceraEntrega/crear_pais.html", contexto) #get


def busqueda_pais(request):
    pais = request.GET["pais"]
    paises = Pais.objects.filter(pais__contains=pais)
    contexto = {
        "paises": paises,
        "form": BusquedaPaisForm(),
    }
    return render(request, "AppTerceraEntrega/paises.html", contexto)

def crear_equipo(request):
    equipo = Equipo(equipo="Barcelona", liga="Española")
    equipo.save()

    return redirect("/app/crear_equipo")  # get

def crear_equipo_form(request):

    if request.method == "POST":
        equipo_formulario = EquipoForm(request.POST)
        if equipo_formulario.is_valid():
            informacion = equipo_formulario.cleaned_data
            equipo_crear = Equipo(equipo=informacion["equipo"], liga=informacion["liga"])
            equipo_crear.save()
            return redirect("/app/equipos/")

    equipo_formulario = EquipoForm()
    contexto = {
        "form": equipo_formulario
    }
    return render(request, "AppTerceraEntrega/crear_equipo.html", contexto) #get

def crear_estadio(request):
    estadio = Estadio(estadio="Camp Nou")
    estadio.save()

    return redirect("/app/crear_estadio")  # get

def crear_estadio_form(request):

    if request.method == "POST":
        estadio_formulario = EstadioForm(request.POST)
        if estadio_formulario.is_valid():
            informacion = estadio_formulario.cleaned_data
            estadio_crear = Estadio(estadio=informacion["estadio"])
            estadio_crear.save()
            return redirect("/app/estadios/")

    estadio_formulario = EstadioForm()
    contexto = {
        "form": estadio_formulario
    }
    return render(request, "AppTerceraEntrega/crear_estadio.html", contexto) #get

def show_html(request):
    paises = Pais.objects.all()
    contexto = {
        "paises": paises,
    }
    return render(request, "index.html", contexto)





