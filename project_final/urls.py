from django.urls import path, include
from . import views

# Create your views here.

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lo_mejor/', views.lo_mejor, name='lo_mejor'),
    path('historias_beats/', views.historias_beats, name='historias_beats'),
    path('registrar_apostadores/', views.registrar_apostadores, name='registrar_apostadores'),  
    path('registrar_caracteristicas/<int:apostador_id>/', views.registrar_caracteristicas, name='registrar_caracteristicas'),
    path('eliminar_apostador/<int:id>', views.eliminar_apostador, name='eliminar_apostador'),
    path('lista_apostadores/', views.lista_apostadores, name='lista_apostadores'),
    path('info_apostador/<int:id>', views.info_apostador, name='info_apostador'),
]