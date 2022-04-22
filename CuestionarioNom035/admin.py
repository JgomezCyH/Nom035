from django.contrib import admin

from .models import Categoria, Dominio, Dimension, Reactivo, Cuestionario, CuestPregunta, RespCuestPregunta, \
    Cuestionario72


# Register your models here.


class CategoriaView(admin.ModelAdmin):
    list_display = ('id', 'categoria')


class DominioView(admin.ModelAdmin):
    list_display = ('id', 'dominio', 'categoria')


class DimensionView(admin.ModelAdmin):
    list_display = ('id', 'dimension', 'dominio')


class ReactivoView(admin.ModelAdmin):
    list_display = ('numero', 'pregunta', 'dimension')


class CuestPreguntaView(admin.ModelAdmin):
    list_display = ('cuestionario', 'reactivo')


class Cuestionario72View(admin.ModelAdmin):
    list_display = (
        'Nombre',
        'EstadoCivil',
        'Edad',
        'Puesto',
        'Escolaridad',
        'T1',
        'T2',
        'T3',
        'T4',
        'T5',
        'T6',
        'T7',
        'T8',
        'T9',
        'T10',
        'T11',
        'T12',
        'T13',
        'T14',
        'T15',
        'T16',
        'T17',
        'T18',
        'T19',
        'T20',
        'p1',
        'p2',
        'p3',
        'p4',
        'p5',
        'p6',
        'p7',
        'p8',
        'p9',
        'p10',
        'p11',
        'p12',
        'p13',
        'p14',
        'p15',
        'p16',
        'p17',
        'p18',
        'p19',
        'p20',
        'p21',
        'p22',
        'p23',
        'p24',
        'p25',
        'p26',
        'p27',
        'p28',
        'p29',
        'p30',
        'p31',
        'p32',
        'p33',
        'p34',
        'p35',
        'p36',
        'p37',
        'p38',
        'p39',
        'p40',
        'p41',
        'p42',
        'p43',
        'p44',
        'p45',
        'p46',
        'p47',
        'p48',
        'p49',
        'p50',
        'p51',
        'p52',
        'p53',
        'p54',
        'p55',
        'p56',
        'p57',
        'p58',
        'p59',
        'p60',
        'p61',
        'p62',
        'p63',
        'p64',
        'p65',
        'p66',
        'p67',
        'p68',
        'p69',
        'p70',
        'p71',
        'p72'
    )


# admin.site.register(Categoria, CategoriaView)
# admin.site.register(Dominio, DominioView)
# admin.site.register(Dimension, DimensionView)
# admin.site.register(Reactivo, ReactivoView)
# admin.site.register(Cuestionario, CuestionarioView)
# admin.site.register(CuestPregunta,CuestPreguntaView)
# admin.site.register(RespCuestPregunta)
admin.site.register(Cuestionario72, Cuestionario72View)
