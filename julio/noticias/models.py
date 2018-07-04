# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Noticias(models.Model):
    foto = models.ImageField(upload_to='media')
    introduccion = models.CharField('introduccion', max_length=50)
    descripcion = models.CharField('descripcion', max_length=200)
    
    def promedio(self):
        noticia = Puntaje.objects.filter(noticia = self)
        cant= 0
        for m in noticias:
            cant += 1
            total += m.puntaje

        prom = total/cant

        return prom

    def __str__(self):
            return '{} {} {} '.format(self.foto, self.introduccion, self.descripcion)

class Puntaje(models.Model):
    noticia = models.ForeignKey(Noticias)
    puntaje = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
            return '{} {}  '.format(self.noticia, self.puntaje)