import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from CuestionarioNom035.forms import CuestionarioForm, Cuestionario72Form
from CuestionarioNom035.models import CuestPregunta, Cuestionario72


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def myindex(request):
    return render(request, 'cuestionario.html')


def cuestionario(request):
    data = {
        'form': CuestionarioForm(),
        'preguntas': CuestPregunta.objects.filter(cuestionario=1)
    }
    return render(request, 'index.html', data)


def fin(request):
    data = {
        'form': Cuestionario72Form
    }

    if request.method == 'POST':
        cuestionario = Cuestionario72Form(data=request.POST)
        if cuestionario.is_valid():
            cuestionario.save()
            message = "True"
            return render(request, 'fin.html', {'Message': message, 'cuestionario': cuestionario})
        else:
            message = "False"
            return render(request, 'fin.html', {'Message': message, 'cuestionario': cuestionario})
    return render(request, 'fin.html')


def dashborad(request):
    respuestas = Cuestionario72.objects.all()

    return render(request, 'dashboard.html',
                  {'respuestas': respuestas})


