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
                       'Cedis'

                   )

    search_fields = ['Nombre',
                     'EstadoCivil',
                     'Edad',
                     'Puesto',
                     'Escolaridad',
                     'Cedis']


# admin.site.register(Categoria, CategoriaView)
# admin.site.register(Dominio, DominioView)
# admin.site.register(Dimension, DimensionView)
# admin.site.register(Reactivo, ReactivoView)
# admin.site.register(Cuestionario, CuestionarioView)
# admin.site.register(CuestPregunta,CuestPreguntaView)
# admin.site.register(RespCuestPregunta)
admin.site.register(Cuestionario72, Cuestionario72View)
