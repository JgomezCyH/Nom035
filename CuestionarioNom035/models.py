from django.db import models


# Create your models here.}


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.categoria)


class Dominio(models.Model):
    id = models.AutoField(primary_key=True)
    dominio = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.dominio)


class Dimension(models.Model):
    id = models.AutoField(primary_key=True)
    dimension = models.CharField(max_length=100)
    dominio = models.ForeignKey(Dominio, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.dimension)


class Reactivo(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    pregunta = models.CharField(max_length=100)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.pregunta)


class Cuestionario(models.Model):
    id = models.AutoField(primary_key=True)
    cuestionario = models.CharField(max_length=100)


    def __str__(self):
        txt = "{0}"
        return txt.format(self.cuestionario)


estadosciviles = [
    [0, "Soltero"],
    [1, "Casado"],
    [2, "Divorciado"],
    [3, "Separado"],
    [4, "Viudo"],
    [5, "Union Libre"]
]
nivelestudios = [
    [0, "Primaria"],
    [1, "Secundaria"],
    [2, "Bachillerato"],
    [3, "Licenciatura"],
    [4, "PostGrado"]
]
cedis = [
    [0, "PIQ"],
    [1, "AGS"],
    [2, "PARK V"],
    [3, "SJR"],

]


class CuestPregunta(models.Model):
    cuestionario = models.ForeignKey(Cuestionario,on_delete=models.CASCADE)
    reactivo = models.ForeignKey(Reactivo,on_delete=models.CASCADE)


    def __str__(self):
        txt = "{0}"
        return txt.format(self.reactivo)


class RespCuestPregunta(models.Model):
        id = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=100)
        edad = models.IntegerField()
        puesto = models.CharField(max_length=100)
        estadoCivil = models.IntegerField(choices=estadosciviles)
        niveldeestudio = models.IntegerField(choices=nivelestudios)
        pregunta = models.ForeignKey(CuestPregunta, on_delete=models.CASCADE)
        valor = models.IntegerField()


class Cuestionario72(models.Model):
    Nombre = models.CharField(max_length=100)
    EstadoCivil = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Puesto = models.CharField(max_length=50)
    Escolaridad = models.CharField(max_length=50)
    Cedis = models.IntegerField(choices=cedis,default=0)
    T1 = models.BooleanField()
    T2 = models.BooleanField()
    T3 = models.BooleanField()
    T4 = models.BooleanField()
    T5 = models.BooleanField()
    T6 = models.BooleanField()
    T7 = models.BooleanField()
    T8 = models.BooleanField()
    T9 = models.BooleanField()
    T10 = models.BooleanField()
    T11 = models.BooleanField()
    T12 = models.BooleanField()
    T13 = models.BooleanField()
    T14 = models.BooleanField()
    T15 = models.BooleanField()
    T16 = models.BooleanField()
    T17 = models.BooleanField()
    T18 = models.BooleanField()
    T19 = models.BooleanField()
    T20 = models.BooleanField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p4 = models.IntegerField()
    p5 = models.IntegerField()
    p6 = models.IntegerField()
    p7 = models.IntegerField()
    p8 = models.IntegerField()
    p9 = models.IntegerField()
    p10 = models.IntegerField()
    p11 = models.IntegerField()
    p12 = models.IntegerField()
    p13 = models.IntegerField()
    p14 = models.IntegerField()
    p15 = models.IntegerField()
    p16 = models.IntegerField()
    p17 = models.IntegerField()
    p18 = models.IntegerField()
    p19 = models.IntegerField()
    p20 = models.IntegerField()
    p21 = models.IntegerField()
    p22 = models.IntegerField()
    p23 = models.IntegerField()
    p24 = models.IntegerField()
    p25 = models.IntegerField()
    p26 = models.IntegerField()
    p27 = models.IntegerField()
    p28 = models.IntegerField()
    p29 = models.IntegerField()
    p30 = models.IntegerField()
    p31 = models.IntegerField()
    p32 = models.IntegerField()
    p33 = models.IntegerField()
    p34 = models.IntegerField()
    p35 = models.IntegerField()
    p36 = models.IntegerField()
    p37 = models.IntegerField()
    p38 = models.IntegerField()
    p39 = models.IntegerField()
    p40 = models.IntegerField()
    p41 = models.IntegerField()
    p42 = models.IntegerField()
    p43 = models.IntegerField()
    p44 = models.IntegerField()
    p45 = models.IntegerField()
    p46 = models.IntegerField()
    p47 = models.IntegerField()
    p48 = models.IntegerField()
    p49 = models.IntegerField()
    p50 = models.IntegerField()
    p51 = models.IntegerField()
    p52 = models.IntegerField()
    p53 = models.IntegerField()
    p54 = models.IntegerField()
    p55 = models.IntegerField()
    p56 = models.IntegerField()
    p57 = models.IntegerField()
    p58 = models.IntegerField()
    p59 = models.IntegerField()
    p60 = models.IntegerField()
    p61 = models.IntegerField()
    p62 = models.IntegerField()
    p63 = models.IntegerField()
    p64 = models.IntegerField()
    p65 = models.IntegerField(null=True,blank=True)
    p66 = models.IntegerField(null=True,blank=True)
    p67 = models.IntegerField(null=True,blank=True)
    p68 = models.IntegerField(null=True,blank=True)
    p69 = models.IntegerField(null=True,blank=True)
    p70 = models.IntegerField(null=True,blank=True)
    p71 = models.IntegerField(null=True,blank=True)
    p72 = models.IntegerField(null=True,blank=True)




