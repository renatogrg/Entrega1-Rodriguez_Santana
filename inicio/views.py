from inicio.models import Carro
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Create your views here.

def mi_inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    print('PASE POR ACA!!!!!')
    return render(request, 'inicio/about.html')

class ListaCarros(ListView):
    model = Carro
    template_name = 'inicio\lista_carros.html'
    
class CrearCarro(CreateView):
    model = Carro
    template_name = 'inicio\crear_carro.html'
    success_url = reverse_lazy('inicio:listar_carros')
    fields = ['modelo', 'marca', 'precio', 'anio_fabricacion']  
  
class ModificarCarro(LoginRequiredMixin, UpdateView):
    model = Carro
    template_name = 'inicio\modificar_carro.html'
    success_url = reverse_lazy('inicio:listar_carros')
    fields = ['modelo', 'marca', 'precio', 'anio_fabricacion'] 
    
class EliminarCarro(LoginRequiredMixin, DeleteView):
    model = Carro
    template_name = 'inicio\eliminar_carro.html'
    success_url = reverse_lazy('inicio:listar_carros')
    
class MostrarCarro(DetailView):
    model = Carro
    template_name = 'inicio/mostrar_carro.html'