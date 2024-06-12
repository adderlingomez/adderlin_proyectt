from django.urls import path, include
from . import views
from django.contrib import admin
 
from .views import actualizar_apostador
# Create your views here.

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.vista_logout, name='logout'),
    path('', views.inicio, name='inicio'),
    path('lo_mejor/', views.lo_mejor, name='lo_mejor'),
    path('historias_beats/', views.historias_beats, name='historias_beats'),
    path('registrar_apostadores/', views.registrar_apostadores, name='registrar_apostadores'),  
    path('registrar_caracteristicas/<int:apostador_id>/', views.registrar_caracteristicas, name='registrar_caracteristicas'),
    path('eliminar_apostador/<int:id>', views.eliminar_apostador, name='eliminar_apostador'),
    path('lista_apostadores/', views.lista_apostadores, name='lista_apostadores'),
    path('apostador/<int:apostador_id>/actualizar/', views.actualizar_apostador, name='actualizar_apostador'),
     path('info_apostador/<int:id>', views.info_apostador, name='info_apostador'),
    path('terminos-condiciones/', views.terminos_condiciones, name='terminos_condiciones'),
    path('politica-privacidad/', views.politica_privacidad, name='politica_privacidad'),
    path('juego-responsable/', views.juego_responsable, name='juego_responsable'),
   ] 