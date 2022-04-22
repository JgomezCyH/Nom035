from django.urls import path

from . import views

urlpatterns = [
    path('', views.myindex, name='index'),
    path('form', views.cuestionario, name='prueba'),
    path('dashboard',views.dashborad,name='dashboard'),
    path('fin/',views.fin,name='fin')
]
