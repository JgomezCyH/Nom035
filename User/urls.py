from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
urlpatterns = [
path('', views.Login.as_view(), name='login'),

]