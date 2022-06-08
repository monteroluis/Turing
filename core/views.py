from django.shortcuts import render

import principal
from .forms import ValidateForm
from django.http import HttpResponse
from principal import *


def home(request):
    return render(request, "core/index.html")


def buscar(request):
    if request.method == "POST":
        mensaje = request.POST.get("code")
        input = mensaje
        instrucciones = g.parse(input)
        ts_global = TS.TablaDeSimbolos()
        procesar_instrucciones(instrucciones, ts_global)
        imprimir=salida().replace('\n', '<br>')
    return HttpResponse(imprimir)
