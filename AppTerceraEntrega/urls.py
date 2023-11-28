from django.urls import path
from AppTerceraEntrega.views import crear_pais, crear_equipo, crear_estadio, show_html, crear_pais_form, mostrar_paises, \
<<<<<<< HEAD
    busqueda_pais, crear_equipo_form, mostrar_equipos, crear_estadio_form, mostrar_estadios
=======
    busqueda_pais
>>>>>>> a0e8d31d9f18fd347ffc70095e488d6848c4ed2e

urlpatterns = [
    path("agregar_pais/", crear_pais),
    path("pais/", crear_pais_form),
    path("paises/", mostrar_paises),
    path("buscar/", busqueda_pais),
    path("agregar_equipo/", crear_equipo),
    path("equipo/", crear_equipo_form),
    path("equipos/", mostrar_equipos),
    path("agregar_estadio/", crear_estadio),
<<<<<<< HEAD
    path("estadio/", crear_estadio_form),
    path("estadios/", mostrar_estadios),
=======
>>>>>>> a0e8d31d9f18fd347ffc70095e488d6848c4ed2e
    path("", show_html),
]
