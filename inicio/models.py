from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Carro(models.Model):
    modelo = models.CharField(max_length=80)
    marca = models.CharField(max_length=80)
    descripcion=RichTextField(blank=True)
    precio = models.IntegerField()
    anio_fabricacion = models.IntegerField()
    

    def __str__(self):
        return f'El carro de modelo "{self.modelo}" es de la marca "{self.marca}" tiene el precio de "{self.precio} dolares" y su fabricación es del año "{self.anio_fabricacion}"'
    
