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
    df = pd.DataFrame(Cuestionario72.objects.all().values())
    df = df.set_index('id')
    df = df.fillna(0)
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
    df = df.replace({True: 1, False: 0})

    df['Resultado'] = df['T1'] + df['T2'] + df['T3'] + df['T4'] + df['T5'] + df['T6'] + df['T7'] + df['T8'] + df['T9'] + \
                      df['T10'] + df['T11'] + df['T12'] + df['T13'] + df['T14'] + df['T15'] + df['T16'] + df['T17'] + \
                      df['T18'] + df['T19'] + df['T20']

    #df.to_csv(r'C:\Users\Jose Manuel\Desktop\prueba.csv', index=False)
    return render(request, 'dashboard.html',
                  {'respuestas': respuestas, 'dataframe': df.to_dict('records')})
