from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppTerceraEntrega.models import Pais, Equipo, Estadio
from AppTerceraEntrega.forms import PaisForm

#def mostrar_paises(request):
#    paises = Pais.objects.all()
#    contexto = {
#        "paises": paises,
#        "nombre": "España"
#    }

# Create your views here.
def crear_pais(request):
    pais = Pais(pais="España", continente="Europa")
    pais.save()

    return redirect("/app/paises")  # get

def crear_pais_form(request):
    pais_formulario = PaisForm()
    contexto = {
        "form": pais_formulario
    }
    return render(request, "AppTerceraEntrega/crear_pais.html", contexto)


def crear_equipo(request):
    equipo = Equipo(equipo="Barcelona", liga="Española")
    equipo.save()

    return HttpResponse(f"El esquipo es {equipo.equipo} de la Liga {equipo.liga}")

def crear_estadio(request):
    estadio = Estadio(estadio="Camp Nou")
    estadio.save()

    return HttpResponse(f"El estadio es {estadio.estadio}")

def show_html(request):
    contexto = {}
    return render(request, "index.html", contexto)





