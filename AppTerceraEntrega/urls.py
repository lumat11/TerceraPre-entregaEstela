from django.urls import path
from AppTerceraEntrega.views import crear_pais, crear_equipo, crear_estadio, show_html, crear_pais_form, mostrar_paises, \
    busqueda_pais

urlpatterns = [
    path("agregar_pais/", crear_pais),
    path("pais/", crear_pais_form),
    path("paises/", mostrar_paises),
    path("buscar/", busqueda_pais),
    path("agregar_equipo/", crear_equipo),
    path("agregar_estadio/", crear_estadio),
    path("", show_html),
]
