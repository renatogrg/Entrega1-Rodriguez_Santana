from django import forms


class BaseCarroFormulario(forms.Form):
    modelo = forms.CharField(max_length=80)
    marca = forms.CharField(max_length=80)
    precio = forms.IntegerField()
    anio_fabricacion = forms.IntegerField()

class CreacionCarroFormulario(BaseCarroFormulario):
    ...
    
class ModificarCarroFormulario(BaseCarroFormulario):
    ...
    
    
    
class BuscarCarro(forms.Form):
    modelo = forms.CharField(max_length=80, required=False)
    
# class ModificarAnimalFormulario(forms.Form):
        