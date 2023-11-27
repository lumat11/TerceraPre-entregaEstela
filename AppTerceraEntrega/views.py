from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppTerceraEntrega.models import Pais, Equipo, Estadio
from AppTerceraEntrega.forms import PaisForm, BusquedaPaisForm


def mostrar_paises(request):
    paises = Pais.objects.all()
    contexto = {
        "paises": paises,
        "form": BusquedaPaisForm()
    }
    return render(request, "AppTerceraEntrega/paises.html", contexto)

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

    return HttpResponse(f"El esquipo es {equipo.equipo} de la Liga {equipo.liga}")

def crear_estadio(request):
    estadio = Estadio(estadio="Camp Nou")
    estadio.save()

    return HttpResponse(f"El estadio es {estadio.estadio}")

def show_html(request):
    paises = Pais.objects.all()
    contexto = {
        "paises": paises,
    }
    return render(request, "index.html", contexto)





