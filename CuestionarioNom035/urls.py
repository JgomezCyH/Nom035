from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.myindex, name='index'),
    path('dashboard',login_required(views.dashborad),name='dashboard'),
    path('fin/',views.fin,name='fin')
]
