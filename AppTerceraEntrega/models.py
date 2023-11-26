from django.db import models


class Pais(models.Model):
    pais = models.CharField(max_length=30)
    continente = models.CharField(max_length=30)

    def __str__(self):
        return f"País: {self.pais}, Continente: {self.continente}"


class Equipo(models.Model):
    equipo = models.CharField(max_length=30, default='ValorPorDefecto')
    liga = models.CharField(max_length=30, default='ValorPorDefecto')

    def __str__(self):
        return f"Equipo: {self.equipo}, Liga: {self.liga}"


class Estadio(models.Model):
    estadio = models.CharField(max_length=30, default='ValorPorDefecto')

    def __str__(self):
        return f"Estadio: {self.estadio}"

