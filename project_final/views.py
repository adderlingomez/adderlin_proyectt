from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import apostadores, Caracteristica_apostadores
from .forms import FormRegistrarApostador, FormCaracteristicaApostadores
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout 




class LoginView(LoginView):
    template_name = 'login.html'
    Authentication_Form = AuthenticationForm
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = self .Authentication_Form()
        return context
    


def vista_logout(request):
    logout(request)
    
    return redirect('login')







@login_required
def inicio(request):
    return render(request, 'inicio.html')

@login_required
def lo_mejor(request):
    return render(request, 'lo_mejor.html')


@login_required
def historias_beats(request):
    return render(request, 'historias_beats.html')

@login_required
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
@login_required
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




@login_required
def lista_apostadores(request):
    registros_apostadores = apostadores.objects.all()
    return render (request, 'apostadores_lista.html', {
        'apostadores': registros_apostadores
    } )

@login_required
def info_apostador(request, id):
    apostador = apostadores.objects.get(id=id)
    return render(request, "info_apostadores.html", {
        'apostador': apostador
    })


@login_required
def eliminar_apostador(request, id):
    apostador = apostadores.objects.get(id=id)
    apostador.delete()
    return redirect('lista_apostadores')
