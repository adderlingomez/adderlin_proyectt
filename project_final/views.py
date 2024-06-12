from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import FormRegistrarApostador, FormCaracteristicaApostadores, FormActualizarApostador
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Apostador, CaracteristicaApostador, ActualizacionApostador

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    next_page = 'inicio' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = self.authentication_form()
        return context

def vista_logout(request):
    logout(request)
    return redirect('login')

def inicio(request):
    return render(request, 'inicio.html')

def lo_mejor(request):
    return render(request, 'lo_mejor.html')

def historias_beats(request):
    return render(request, 'historias_beats.html')


@login_required
def registrar_apostadores(request):
    if request.method == 'POST':
        form = FormRegistrarApostador(request.POST)
        if form.is_valid():
           apostador = form.save()

           return redirect('registrar_caracteristicas', apostador_id=apostador.id)
            
        else:
            form = FormRegistrarApostador()
    else:   
        form = FormRegistrarApostador()
        return render(request,'registrar_apostador.html',{
        'formulario' : form})
        
        
@login_required
def registrar_caracteristicas(request, apostador_id):
    apostador = get_object_or_404(Apostador, id=apostador_id)
    
    try:
        caracteristica = CaracteristicaApostador.objects.get(apostador=apostador)
    except CaracteristicaApostador.DoesNotExist:
        caracteristica = None

    if request.method == 'POST':
        if caracteristica:
            form = FormCaracteristicaApostadores(request.POST, instance=caracteristica)
        else:
            form = FormCaracteristicaApostadores(request.POST)
        
        if form.is_valid():
            caracteristica = form.save(commit=False)
            caracteristica.apostador = apostador
            caracteristica.save()
            return redirect('lista_apostadores')
    else:
        form = FormCaracteristicaApostadores(instance=caracteristica)
    
    return render(request, 'registrar_caracteristicas.html', {'form': form, 'apostador': apostador})


def lista_apostadores(request):
    apostadores = Apostador.objects.all()
    return render(request, 'apostadores_lista.html', {'apostadores': apostadores})

def info_apostador(request, id):
    apostador = get_object_or_404(Apostador, id=id)
    return render(request, "info_apostadores.html", {'apostador': apostador})

@login_required
def eliminar_apostador(request, id):
    apostador = get_object_or_404(Apostador, id=id)
    apostador.delete()
    return redirect('lista_apostadores')


@login_required
def actualizar_apostador(request, apostador_id):
    apostador = get_object_or_404(Apostador, pk=apostador_id)
    caracteristica = get_object_or_404(CaracteristicaApostador, apostador=apostador)

    if request.method == 'POST':
        apostador_form = FormRegistrarApostador(request.POST, instance=apostador)
        caracteristica_form = FormCaracteristicaApostadores(request.POST, instance=caracteristica)
        actualizacion_form = FormActualizarApostador(request.POST)

        if apostador_form.is_valid() and caracteristica_form.is_valid() and actualizacion_form.is_valid():
            apostador_form.save()
            caracteristica_form.save()
            actualizacion = actualizacion_form.save(commit=False)
            actualizacion.apostador = apostador
            actualizacion.save()
            return redirect('info_apostador', id=apostador.id)
    else:
        apostador_form = FormRegistrarApostador(instance=apostador)
        caracteristica_form = FormCaracteristicaApostadores(instance=caracteristica)
        actualizacion_form = FormActualizarApostador()

    return render(request, 'actualizar_apostador.html', {
        'apostador_form': apostador_form,
        'caracteristica_form': caracteristica_form,
        'actualizacion_form': actualizacion_form
    })
def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

def politica_privacidad(request):
    return render(request, 'politica-privacidad.html')


def juego_responsable(request):
    return render(request, 'juego_responsable.html')

