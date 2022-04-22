from django import forms
from .models import RespCuestPregunta, Cuestionario72


class CuestionarioForm(forms.ModelForm):
    class Meta:
        model = RespCuestPregunta
        fields = ['nombre', 'edad', 'puesto', 'estadoCivil', 'niveldeestudio']


class Cuestionario72Form(forms.ModelForm):
    class Meta:
        model = Cuestionario72
        fields = '__all__'
