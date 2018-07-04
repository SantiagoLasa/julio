# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from noticias.models import *

# Create your views here.





def index(request):
    noticias = Noticias.objects.all()
    return render(request, "index.html",  {'noticias':noticias})


def ver_mas(request, id_noticias):
    noticia = Noticias.objects.get(id=id_noticias)

    return render(request, "info.html",  {'noticia':noticia})
    
