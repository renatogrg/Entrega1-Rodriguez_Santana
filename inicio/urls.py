from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    
    # path('carros/crear/', views.crear_carro, name='crear_carro'),
    # path('carros/', views.lista_carros, name='listar_carro'),
    # path('carros/eliminar/<int:id_carro>', views.eliminar_carro, name='eliminar_carro'),
    # path('carros/modificar/<int:id_carro>', views.eliminar_carro, name='modificar_carro'),
    
    path('', views.mi_inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('carros/', views.ListaCarros.as_view(), name='listar_carros'),
    path('carros/crear/', views.CrearCarro.as_view(), name='crear_carro'),
    path('carros/<int:pk>/', views.MostrarCarro.as_view(), name='mostrar_carro'),
    path('carros/<int:pk>/eliminar/', views.EliminarCarro.as_view(), name='eliminar_carro'),
    path('carros/<int:pk>/modificar/', views.ModificarCarro.as_view(), name='modificar_carro'),
]   