from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import apostadores, Caracteristica_apostadores
from .forms import FormRegistrarApostador, FormCaracteristicaApostadores



def inicio(request):
    return render(request, 'inicio.html')


def lo_mejor(request):
    return render(request, 'lo_mejor.html')



def historias_beats(request):
    return render(request, 'historias_beats.html')


def registrar_apostadores(request):
    if request.method == 'POST':
        form = FormRegistrarApostador(request.POST)
        if form.is_valid():
            apostador = form.save()

            # caracteristica_form = FormCaracteristicaApostadores(initial={'apostador': apostador})
            return redirect('registrar_caracteristicas', apostador_id=apostador.id)
        
        else:
            form = FormRegistrarApostador()
    else:
        form = FormRegistrarApostador()
    return render(request, 'registrar_apostador.html',{
        'formulario': form})

def registrar_caracteristicas(request, apostador_id):
    apostador = get_object_or_404(apostadores, pk=apostador_id)

    if request.method == 'POST':
        form = FormCaracteristicaApostadores(request.POST)
        if form.is_valid():
            caracteristica = form.save(commit=False)
            caracteristica.apostador = apostador
            caracteristica.save()
            return redirect("lista_apostadores")
    else:
        form = FormCaracteristicaApostadores()
    return render(request, 'registrar_caracteristicas.html', {'formulario': form})

# def editar(request):
#     registro = apostadores.objects.get(id=3)
#     registro.nombre = 'jesus antoni mera'
#     registro.save()
#     return HttpResponse('corregido')





def lista_apostadores(request):
    registros_apostadores = apostadores.objects.all()
    return render (request, 'apostadores_lista.html', {
        'apostadores': registros_apostadores
    } )


def info_apostador(request, id):
    apostador = apostadores.objects.get(id=id)
    return render(request, "info_apostadores.html", {
        'apostador': apostador
    })



def eliminar_apostador(request, id):
    apostador = apostadores.objects.get(id=id)
    apostador.delete()
    return redirect('lista_apostadores')
