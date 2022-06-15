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

    filter1 = df["Cedis"] == "PIQ"
    filter2 = df["Cedis"] == "AGS"
    filter3 = df["Cedis"] == "PARK V"
    filter4 = df["Cedis"] == "SJR"
    totalNombrepie = get_plot(df.TotalNombre.value_counts(), "Resultado Final")
    resultadoNombrepie = get_plot(df.ResultadoNombre.value_counts(), "Resultado Final")
    d1pie = get_plot(df.d1Nombre.value_counts(), "Condiciones en el ambiente de trabajo")
    d2pie = get_plot(df.d2Nombre.value_counts(), "Carga de trabajo")
    d3pie = get_plot(df.d3Nombre.value_counts(), "Falta de control sobre el trabajo")
    d4pie = get_plot(df.d4Nombre.value_counts(), "Jornada de trabajo")
    d5pie = get_plot(df.d5Nombre.value_counts(), "Interferencia en la relación trabajo-familia")
    d6pie = get_plot(df.d6Nombre.value_counts(), "Liderazgo")
    d7pie = get_plot(df.d7Nombre.value_counts(), "Relaciones en el trabajo")
    d8pie = get_plot(df.d8Nombre.value_counts(), "Violencia")
    d9pie = get_plot(df.d9Nombre.value_counts(), "Reconocimiento del desempeño")
    d10pie = get_plot(df.d10Nombre.value_counts(), "Insuficiente sentido de pertenencia e, inestabilidad")
    dc1pie = get_plot(df.c1Nombre.value_counts(), "Ambiente de trabajo")
    dc2pie = get_plot(df.c2Nombre.value_counts(), "Factores propios de la actividad")
    dc3pie = get_plot(df.c3Nombre.value_counts(), "Organización del tiempo de trabajo")
    dc4píe = get_plot(df.c4Nombre.value_counts(), "Liderazgo y relaciones en el trabajo")
    dc5pie = get_plot(df.c5Nombre.value_counts(), "Entorno organizacional")
    # Graficas para el PIQ
    totalNombrePIQpie = get_plot(df.where(filter1).TotalNombre.value_counts(), "Resultado Final")
    resultadoNombrePIQpie = get_plot(df.where(filter1).ResultadoNombre.value_counts(), "Resultado Final")
    d1PIQpie = get_plot(df.where(filter1).d1Nombre.value_counts(), "Condiciones en el ambiente de trabajo")
    d2PIQpie = get_plot(df.where(filter1).d2Nombre.value_counts(), "Carga de trabajo")
    d3PIQpie = get_plot(df.where(filter1).d3Nombre.value_counts(), "Falta de control sobre el trabajo")
    d4PIQpie = get_plot(df.where(filter1).d4Nombre.value_counts(), "Jornada de trabajo")
    d5PIQpie = get_plot(df.where(filter1).d5Nombre.value_counts(), "Interferencia en la relación trabajo-familia")
    d6PIQpie = get_plot(df.where(filter1).d6Nombre.value_counts(), "Liderazgo")
    d7PIQpie = get_plot(df.where(filter1).d7Nombre.value_counts(), "Relaciones en el trabajo")
    d8PIQpie = get_plot(df.where(filter1).d8Nombre.value_counts(), "Violencia")
    d9PIQpie = get_plot(df.where(filter1).d9Nombre.value_counts(), "Reconocimiento del desempeño")
    d10PIQpie = get_plot(df.where(filter1).d10Nombre.value_counts(),
                         "Insuficiente sentido de pertenencia e, inestabilidad")
    dc1PIQpie = get_plot(df.where(filter1).c1Nombre.value_counts(), "Ambiente de trabajo")
    dc2PIQpie = get_plot(df.where(filter1).c2Nombre.value_counts(), "Factores propios de la actividad")
    dc3PIQpie = get_plot(df.where(filter1).c3Nombre.value_counts(), "Organización del tiempo de trabajo")
    dc4PIQpíe = get_plot(df.where(filter1).c4Nombre.value_counts(), "Liderazgo y relaciones en el trabajo")
    dc5PIQpie = get_plot(df.where(filter1).c5Nombre.value_counts(), "Entorno organizacional")

    # Graficas para AGS
    totalNombreAGSpie = get_plot(df.where(filter2).TotalNombre.value_counts(), "Resultado Final")
    resultadoNombreAGSpie = get_plot(df.where(filter2).ResultadoNombre.value_counts(), "Resultado Final")
    d1AGSpie = get_plot(df.where(filter2).d1Nombre.value_counts(), "Condiciones en el ambiente de trabajo")
    d2AGSpie = get_plot(df.where(filter2).d2Nombre.value_counts(), "Carga de trabajo")
    d3AGSpie = get_plot(df.where(filter2).d3Nombre.value_counts(), "Falta de control sobre el trabajo")
    d4AGSpie = get_plot(df.where(filter2).d4Nombre.value_counts(), "Jornada de trabajo")
    d5AGSpie = get_plot(df.where(filter2).d5Nombre.value_counts(), "Interferencia en la relación trabajo-familia")
    d6AGSpie = get_plot(df.where(filter2).d6Nombre.value_counts(), "Liderazgo")
    d7AGSpie = get_plot(df.where(filter2).d7Nombre.value_counts(), "Relaciones en el trabajo")
    d8AGSpie = get_plot(df.where(filter2).d8Nombre.value_counts(), "Violencia")
    d9AGSpie = get_plot(df.where(filter2).d9Nombre.value_counts(), "Reconocimiento del desempeño")
    d10AGSpie = get_plot(df.where(filter2).d10Nombre.value_counts(),
                         "Insuficiente sentido de pertenencia e, inestabilidad")
    dc1AGSpie = get_plot(df.where(filter2).c1Nombre.value_counts(), "Ambiente de trabajo")
    dc2AGSpie = get_plot(df.where(filter2).c2Nombre.value_counts(), "Factores propios de la actividad")
    dc3AGSpie = get_plot(df.where(filter2).c3Nombre.value_counts(), "Organización del tiempo de trabajo")
    dc4AGSpíe = get_plot(df.where(filter2).c4Nombre.value_counts(), "Liderazgo y relaciones en el trabajo")
    dc5AGSpie = get_plot(df.where(filter2).c5Nombre.value_counts(), "Entorno organizacional")

    # Graficas para PARK
    totalNombrePARKpie = get_plot(df.where(filter2).TotalNombre.value_counts(), "Resultado Final")
    resultadoNombrePARKpie = get_plot(df.where(filter2).ResultadoNombre.value_counts(), "Resultado Final")
    d1PARKpie = get_plot(df.where(filter2).d1Nombre.value_counts(), "Condiciones en el ambiente de trabajo")
    d2PARKpie = get_plot(df.where(filter2).d2Nombre.value_counts(), "Carga de trabajo")
    d3PARKpie = get_plot(df.where(filter2).d3Nombre.value_counts(), "Falta de control sobre el trabajo")
    d4PARKpie = get_plot(df.where(filter2).d4Nombre.value_counts(), "Jornada de trabajo")
    d5PARKpie = get_plot(df.where(filter2).d5Nombre.value_counts(), "Interferencia en la relación trabajo-familia")
    d6PARKpie = get_plot(df.where(filter2).d6Nombre.value_counts(), "Liderazgo")
    d7PARKpie = get_plot(df.where(filter2).d7Nombre.value_counts(), "Relaciones en el trabajo")
    d8PARKpie = get_plot(df.where(filter2).d8Nombre.value_counts(), "Violencia")
    d9PARKpie = get_plot(df.where(filter2).d9Nombre.value_counts(), "Reconocimiento del desempeño")
    d10PARKpie = get_plot(df.where(filter2).d10Nombre.value_counts(),
                          "Insuficiente sentido de pertenencia e, inestabilidad")
    dc1PARKpie = get_plot(df.where(filter2).c1Nombre.value_counts(), "Ambiente de trabajo")
    dc2PARKpie = get_plot(df.where(filter2).c2Nombre.value_counts(), "Factores propios de la actividad")
    dc3PARKpie = get_plot(df.where(filter2).c3Nombre.value_counts(), "Organización del tiempo de trabajo")
    dc4PARKpíe = get_plot(df.where(filter2).c4Nombre.value_counts(), "Liderazgo y relaciones en el trabajo")
    dc5PARKpie = get_plot(df.where(filter2).c5Nombre.value_counts(), "Entorno organizacional")
    # Graficas SJR
    totalNombreSJRpie = get_plot(df.where(filter2).TotalNombre.value_counts(), "Resultado Final")
    resultadoNombreSJRpie = get_plot(df.where(filter2).ResultadoNombre.value_counts(), "Resultado Final")
    d1SJRpie = get_plot(df.where(filter2).d1Nombre.value_counts(), "Condiciones en el ambiente de trabajo")
    d2SJRpie = get_plot(df.where(filter2).d2Nombre.value_counts(), "Carga de trabajo")
    d3SJRpie = get_plot(df.where(filter2).d3Nombre.value_counts(), "Falta de control sobre el trabajo")
    d4SJRpie = get_plot(df.where(filter2).d4Nombre.value_counts(), "Jornada de trabajo")
    d5SJRpie = get_plot(df.where(filter2).d5Nombre.value_counts(), "Interferencia en la relación trabajo-familia")
    d6SJRpie = get_plot(df.where(filter2).d6Nombre.value_counts(), "Liderazgo")
    d7SJRpie = get_plot(df.where(filter2).d7Nombre.value_counts(), "Relaciones en el trabajo")
    d8SJRpie = get_plot(df.where(filter2).d8Nombre.value_counts(), "Violencia")
    d9SJRpie = get_plot(df.where(filter2).d9Nombre.value_counts(), "Reconocimiento del desempeño")
    d10SJRpie = get_plot(df.where(filter2).d10Nombre.value_counts(),
                         "Insuficiente sentido de pertenencia e, inestabilidad")
    dc1SJRpie = get_plot(df.where(filter2).c1Nombre.value_counts(), "Ambiente de trabajo")
    dc2SJRpie = get_plot(df.where(filter2).c2Nombre.value_counts(), "Factores propios de la actividad")
    dc3SJRpie = get_plot(df.where(filter2).c3Nombre.value_counts(), "Organización del tiempo de trabajo")
    dc4SJRpíe = get_plot(df.where(filter2).c4Nombre.value_counts(), "Liderazgo y relaciones en el trabajo")
    dc5SJRpie = get_plot(df.where(filter2).c5Nombre.value_counts(), "Entorno organizacional")

    return render(request, 'dashboard.html',
                  {'respuestas': respuestas, 'dataframe': df.to_dict('records'), 'totalNombrepie': totalNombrepie,
                   'resultadoNombrepie': resultadoNombrepie,
                   'd1pie': d1pie, 'd2pie': d2pie,
                   'd3pie': d3pie,
                   'd4pie': d4pie, 'd5pie': d5pie, 'd6pie': d6pie, 'd7pie': d7pie, 'd8pie': d8pie,
                   'd9pie': d9pie, 'd10pie': d10pie, 'dc1pie': dc1pie, 'dc2pie': dc2pie, 'dc3pie': dc3pie,
                   'dc4pie': dc4píe, 'dc5pie': dc5pie,

                   # Graficas de piq
                   'totalNombrePIQpie': totalNombrePIQpie,
                   'resultadoNombrePIQpie': resultadoNombrePIQpie,
                   'd1PIQpie': d1PIQpie, 'd2PIQpie': d2PIQpie,
                   'd3PIQpie': d3PIQpie,
                   'd4PIQpie': d4PIQpie, 'd5PIQpie': d5PIQpie, 'd6PIQpie': d6PIQpie, 'd7PIQpie': d7PIQpie,
                   'd8PIQpie': d8PIQpie,
                   'd9PIQpie': d9PIQpie, 'd10PIQpie': d10PIQpie, 'dc1PIQpie': dc1PIQpie, 'dc2PIQpie': dc2PIQpie,
                   'dc3PIQpie': dc3PIQpie,
                   'dc4PIQpie': dc4PIQpíe, 'dc5PIQpie': dc5PIQpie,
                   # Graficas de aguascalientes
                   'totalNombreAGSpie': totalNombreAGSpie,
                   'resultadoNombreAGSpie': resultadoNombreAGSpie,
                   'd1AGSpie': d1AGSpie, 'd2AGSpie': d2AGSpie,
                   'd3AGSpie': d3AGSpie,
                   'd4AGSpie': d4AGSpie, 'd5AGSpie': d5AGSpie, 'd6AGSpie': d6AGSpie, 'd7AGSpie': d7AGSpie,
                   'd8AGSpie': d8AGSpie,
                   'd9AGSpie': d9AGSpie, 'd10AGSpie': d10AGSpie, 'dc1AGSpie': dc1AGSpie, 'dc2AGSpie': dc2AGSpie,
                   'dc3AGSpie': dc3AGSpie,
                   'dc4AGSpie': dc4AGSpíe, 'dc5AGSpie': dc5AGSpie,

                   # Graficas de PARK V
                   'totalNombrePARKpie': totalNombrePARKpie,
                   'resultadoNombrePARKpie': resultadoNombrePARKpie,
                   'd1PARKpie': d1PARKpie, 'd2PARKpie': d2PARKpie,
                   'd3PARKpie': d3PARKpie,
                   'd4PARKpie': d4PARKpie, 'd5PARKpie': d5PARKpie, 'd6PARKpie': d6PARKpie, 'd7PARKpie': d7PARKpie,
                   'd8PARKpie': d8PARKpie,
                   'd9PARKpie': d9PARKpie, 'd10PARKpie': d10PARKpie, 'dc1PARKpie': dc1PARKpie, 'dc2PARKpie': dc2PARKpie,
                   'dc3PARKpie': dc3PARKpie,
                   'dc4PARKpie': dc4PARKpíe, 'dc5PARKpie': dc5PARKpie,

                   # Graficas de SJR
                   'totalNombreSJRpie': totalNombreSJRpie,
                   'resultadoNombreSJRpie': resultadoNombreSJRpie,
                   'd1SJRpie': d1SJRpie, 'd2SJRpie': d2SJRpie,
                   'd3SJRpie': d3SJRpie,
                   'd4SJRpie': d4SJRpie, 'd5SJRpie': d5SJRpie, 'd6SJRpie': d6SJRpie, 'd7SJRpie': d7SJRpie,
                   'd8SJRpie': d8SJRpie,
                   'd9SJRpie': d9SJRpie, 'd10SJRpie': d10SJRpie, 'dc1SJRpie': dc1SJRpie, 'dc2SJRpie': dc2SJRpie,
                   'dc3SJRpie': dc3SJRpie,
                   'dc4SJRpie': dc4SJRpíe, 'dc5SJRpie': dc5SJRpie

                   })
