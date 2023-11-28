from django.urls import path
from AppTerceraEntrega.views import crear_pais, busqueda_pais, crear_estadio, show_html, crear_pais_form, \
    mostrar_paises, crear_equipo, crear_equipo_form, mostrar_equipos, crear_estadio_form, mostrar_estadios

urlpatterns = [
    path("agregar_pais/", crear_pais),
    path("pais/", crear_pais_form),
    path("paises/", mostrar_paises),
    path("buscar/", busqueda_pais),
    path("agregar_equipo/", crear_equipo),
    path("equipo/", crear_equipo_form),
    path("equipos/", mostrar_equipos),
    path("agregar_estadio/", crear_estadio),
    path("estadio/", crear_estadio_form),
    path("estadios/", mostrar_estadios),
    path("", show_html),
]
