from django.http import HttpResponse
from django.shortcuts import render
from AppTerceraEntrega.models import Pais, Equipo, Estadio


# Create your views here.
def crear_pais(request):
    pais = Pais(pais="España", continente="Europa")
    pais.save()

    return HttpResponse(f"Su país es {pais.pais} del continente {pais.continente}")

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





