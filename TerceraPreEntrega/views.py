from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Tercera Pre-entrega")

def plantilla(request):
    contexto = {}
    return render(request,"index.html", contexto)