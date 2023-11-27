from django.urls import path
from AppTerceraEntrega.views import crear_pais, crear_equipo, crear_estadio, show_html, crear_pais_form

urlpatterns = [
    path("agregar_pais/", crear_pais),
    path("pais/", crear_pais_form),
    path("agregar_equipo/", crear_equipo),
    path("agregar_estadio/", crear_estadio),
    path("show/", show_html),
]
