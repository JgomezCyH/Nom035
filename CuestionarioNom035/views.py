import base64
from io import BytesIO

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from matplotlib import pyplot as plt

from CuestionarioNom035.forms import CuestionarioForm, Cuestionario72Form
from CuestionarioNom035.models import CuestPregunta, Cuestionario72
from CuestionarioNom035.utils import get_graph, get_plot


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
    df = pd.DataFrame(Cuestionario72.objects.all().values())
    df = df.set_index('id')
    df = df.fillna(0)
    df = df.replace({True: 0, False: 0})
    df = df.drop_duplicates()
    df['Puesto'] = df['Puesto'].str.upper()

    df['d1'] = df['p1'] + df['p2'] + df['p3'] + df['p4'] + df['p5']
    df['d2'] = df['p6'] + df['p12'] + df['p7'] + df['p8'] + df['p9'] + df['p10'] + df['p11'] + df['p65'] + df['p66'] + \
               df['p67'] + df['p68'] + df['p13'] + df['p14'] + df['p15'] + df['p16']
    df['d3'] = df['p25'] + df['p26'] + df['p27'] + df['p28'] + df['p23'] + df['p24'] + df['p29'] + df['p30'] + df[
        'p35'] + df['p36']
    df['d4'] = df['p17'] + df['p18']
    df['d5'] = df['p19'] + df['p20'] + df['p21'] + df['p22']
    df['d6'] = df['p31'] + df['p32'] + df['p33'] + df['p34'] + df['p37'] + df['p38'] + df['p39'] + df['p40'] + df['p41']
    df['d7'] = df['p42'] + df['p43'] + df['p44'] + df['p45'] + df['p46'] + df['p69'] + df['p70'] + df['p71'] + df['p72']
    df['d8'] = df['p57'] + df['p58'] + df['p59'] + df['p60'] + df['p61'] + df['p62'] + df['p63'] + df['p64']
    df['d9'] = df['p47'] + df['p48'] + df['p49'] + df['p50'] + df['p51'] + df['p52']
    df['d10'] = df['p55'] + df['p56'] + df['p53'] + df['p54']
    df['c1'] = df['d1']
    df['c2'] = df['d2'] + df['d3']
    df['c3'] = df['d4'] + df['d5']
    df['c4'] = df['d6'] + df['d7'] + df['d8']
    df['c5'] = df['d9'] + df['d10']
    df['Total'] = df['c1'] + df['c2'] + df['c3'] + df['c4'] + df['c5']

    df['Resultado'] = df['T1'] + df['T2'] + df['T3'] + df['T4'] + df['T5'] + df['T6'] + df['T7'] + df['T8'] + df['T9'] + \
                      df['T10'] + df['T11'] + df['T12'] + df['T13'] + df['T14'] + df['T15'] + df['T16'] + df['T17'] + \
                      df['T18'] + df['T19'] + df['T20']
    df['TotalNombre'] = df['Total']
    df['ResultadoNombre'] = df['Resultado']
    df['d1Nombre'] = df['d1']
    df['d2Nombre'] = df['d2']
    df['d3Nombre'] = df['d3']
    df['d4Nombre'] = df['d4']
    df['d5Nombre'] = df['d5']
    df['d6Nombre'] = df['d6']
    df['d7Nombre'] = df['d7']
    df['d8Nombre'] = df['d8']
    df['d9Nombre'] = df['d9']
    df['d10Nombre'] = df['d10']
    df['c1Nombre'] = df['c1']
    df['c2Nombre'] = df['c2']
    df['c3Nombre'] = df['c3']
    df['c4Nombre'] = df['c4']
    df['c5Nombre'] = df['c5']
    df.d1Nombre = pd.cut(df.d1,
                         bins=[-1, 4, 8, 10, 13, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d2Nombre = pd.cut(df.d2,
                         bins=[-1, 14, 20, 26, 36, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d3Nombre = pd.cut(df.d3,
                         bins=[-1, 10, 15, 20, 24, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d4Nombre = pd.cut(df.d4,
                         bins=[-1, 0, 1, 3, 5, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d5Nombre = pd.cut(df.d5,
                         bins=[-1, 3, 5, 7, 9, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d6Nombre = pd.cut(df.d6,
                         bins=[-1, 8, 11, 15, 19, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d7Nombre = pd.cut(df.d7,
                         bins=[-1, 9, 12, 16, 20, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d8Nombre = pd.cut(df.d8,
                         bins=[-1, 6, 9, 12, 15, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d9Nombre = pd.cut(df.d9,
                         bins=[-1, 5, 9, 13, 17, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.d10Nombre = pd.cut(df.d10,
                          bins=[-1, 3, 5, 7, 10, 100],
                          labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.c1Nombre = pd.cut(df.c1,
                         bins=[-1, 4, 8, 10, 13, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.c2Nombre = pd.cut(df.c2,
                         bins=[-1, 14, 28, 41, 57, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.c3Nombre = pd.cut(df.c3,
                         bins=[-1, 4, 6, 9, 12, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.c4Nombre = pd.cut(df.c4,
                         bins=[-1, 13, 28, 41, 57, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.c5Nombre = pd.cut(df.c5,
                         bins=[-1, 9, 13, 17, 23, 100],
                         labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.TotalNombre = pd.cut(df.Total,
                            bins=[0, 49, 74, 98, 139, 1000],
                            labels=['Nulo o despreciable', 'Bajo', 'Medio', 'Alto', 'Muy alto'])
    df.ResultadoNombre = pd.cut(df.Resultado,
                                bins=[-1, 10, 20],
                                labels=['No Requiere Atencion', 'Requiere Atencion'])
    # df.to_csv(r'C:\Users\Jose Manuel\Desktop\prueba.csv', index=False)

    totalNombrepie = get_plot(df.TotalNombre.value_counts(), "Resultado Final",
                              colors=['#6BF56E', '#FFFF00', '#9BE5F7', '#FFC000', 'red'],
                              legends={'Bajo': '#6BF56E', 'Medio': '#FFFF00', 'Nulo': '#9BE5F7', 'Alto': '#FFC000',
                                       'Muy Alto': 'red'})
    resultadoNombrepie = get_plot(df.ResultadoNombre.value_counts(), "Resultado Final",
                              colors=[ '#9BE5F7',  'red'],
                              legends={'No Requiere Atencion Medica': '#6BF56E',
                                       'Requiere Atencion Medica': 'red'})

    d1pie = get_plot(df.d1Nombre.value_counts(), "Condiciones en el ambiente de trabajo",
                     colors=['#9BE5F7', '#6BF56E', '#FFFF00', '#FFC000', 'red'],
                     legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Medio': '#FFFF00', 'Alto': '#FFC000',
                              'Muy Alto': 'red'})
    d2pie = get_plot(df.d2Nombre.value_counts(), "Carga de trabajo",
                     colors=['#FFC000', '#9BE5F7', '#FFFF00', '#6BF56E', 'red'],
                     legends={'Alto': '#FFC000', 'Nulo': '#9BE5F7', 'Medio': '#FFFF00', 'Bajo': '#6BF56E',
                              'Muy Alto': 'red'})
    d3pie = get_plot(df.d3Nombre.value_counts(), "Falta de control sobre el trabajo",
                     colors=['#9BE5F7', '#6BF56E', '#FFFF00', '#FFC000', 'red'],
                     legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Medio': '#FFFF00', 'Alto': '#FFC000',
                              'Muy Alto': 'red'})
    d4pie = get_plot(df.d4Nombre.value_counts(), "Jornada de trabajo",
                     colors=['#9BE5F7', '#FFFF00', 'red', '#FFC000', '#6BF56E'],
                     legends={'Nulo': '#9BE5F7', 'Medio': '#FFFF00', 'Muy Alto': 'red', 'Alto': '#FFC000',
                              'Bajo': '#6BF56E'})
    d5pie = get_plot(df.d5Nombre.value_counts(), "Interferencia en la relación trabajo-familia",
                     colors=['#9BE5F7', '#6BF56E', '#FFFF00', '#FFC000', 'red'],
                     legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Medio': '#FFFF00', 'Alto': '#FFC000',
                              'Muy Alto': 'red'})
    d6pie = get_plot(df.d6Nombre.value_counts(), "Liderazgo",
                     colors=['#9BE5F7', 'red', '#FFFF00', '#FFC000', '#6BF56E'],
                     legends={'Nulo': '#9BE5F7', 'Muy Alto': 'red', 'Medio': '#FFFF00', 'Alto': '#FFC000',
                              'Bajo': '#6BF56E'})
    d7pie = get_plot(df.d7Nombre.value_counts(), "Relaciones en el trabajo",
                     colors=['#9BE5F7', '#FFFF00', '#6BF56E', '#FFC000', 'red'],
                     legends={'Nulo': '#9BE5F7', 'Medio': '#FFFF00', 'Bajo': '#6BF56E', 'Alto': '#FFC000',
                              'Muy Alto': 'red'})
    d8pie = get_plot(df.d8Nombre.value_counts(), "Violencia",
                     colors=['#9BE5F7', '#6BF56E', '#FFFF00', 'red', '#FFC000'],
                     legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Alto': '#FFFF00', 'Muy Alto': 'red',
                              'Medio': '#FFC000',
                              })
    d9pie = get_plot(df.d9Nombre.value_counts(), "Reconocimiento del desempeño",
                     colors=['#9BE5F7', '#6BF56E', '#FFFF00', '#FFC000', 'red'],
                     legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Alto': '#FFFF00',
                              'Medio': '#FFC000', 'Muy Alto': 'red'
                              })
    d10pie = get_plot(df.d10Nombre.value_counts(), "Insuficiente sentido de pertenencia e, inestabilidad",
                      colors=['#6BF56E', '#9BE5F7', '#FFFF00', '#FFC000', 'red'],
                      legends={'Bajo': '#6BF56E', 'Nulo': '#9BE5F7', 'Alto': '#FFFF00',
                               'Medio': '#FFC000', 'Muy Alto': 'red'
                               })
    dc1pie = get_plot(df.c1Nombre.value_counts(), "Ambiente de trabajo",
                      colors=['#9BE5F7', '#6BF56E', '#FFFF00', '#FFC000', 'red'],
                      legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Medio': '#FFFF00', 'Alto': '#FFC000',
                               'Muy Alto': 'red'})

    dc2pie = get_plot(df.c2Nombre.value_counts(), "Factores propios de la actividad",
                      colors=['#FFFF00', '#6BF56E', '#FFC000', '#9BE5F7', 'red'],
                      legends={'Medio': '#FFFF00', 'Bajo': '#6BF56E', 'Alto': '#FFC000', 'Nulo': '#9BE5F7',
                               'Muy Alto': 'red'})
    dc3pie = get_plot(df.c3Nombre.value_counts(), "Organización del tiempo de trabajo",
                      colors=['#9BE5F7', '#FFF000', '#6BF56E', '#FFC000', 'red'],
                      legends={'Nulo': '#9BE5F7', 'Medio': '#FFFF00', 'Bajo': '#6BF56E', 'Alto': '#FFC000',
                               'Muy Alto': 'red'})
    dc4íe = get_plot(df.c4Nombre.value_counts(), "Liderazgo y relaciones en el trabajo",
                     colors=['#9BE5F7', '#6BF56E', '#FFC000', '#FFF000', 'red'],
                     legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Alto': '#FFC000', 'Medio': '#FFFF00',
                              'Muy Alto': 'red'})
    dc5pie = get_plot(df.c5Nombre.value_counts(), "Entorno organizacional",
                      colors=['#9BE5F7', '#6BF56E', '#FFF000', '#FFC000', 'red'],
                      legends={'Nulo': '#9BE5F7', 'Bajo': '#6BF56E', 'Medio': '#FFFF00', 'Alto': '#FFC000',
                               'Muy Alto': 'red'})

    return render(request, 'dashboard.html',
                  {'respuestas': respuestas, 'dataframe': df.to_dict('records'), 'totalNombrepie': totalNombrepie,
                   'resultadoNombrepie':resultadoNombrepie,
                   'd1pie': d1pie, 'd2pie': d2pie,
                   'd3pie': d3pie,
                   'd4pie': d4pie, 'd5pie': d5pie, 'd6pie': d6pie, 'd7pie': d7pie, 'd8pie': d8pie,
                   'd9pie': d9pie, 'd10pie': d10pie, 'dc1pie':dc1pie,'dc2pie':dc2pie,'dc3pie':dc3pie,
                   'dc4pie':dc4íe,'dc5pie':dc5pie})
