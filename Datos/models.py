from django.db import models

# Create your models here.
class Unidad_Medida(models.Model):
    descripcion=models.CharField(max_length=100)
    abreviacion=models.CharField(max_length=20, null=True , blank=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name='Unidad de medida'
        verbose_name_plural='Unidades de medida'

class Material(models.Model):
    descripcion=models.CharField(max_length=100)
    precio=models.FloatField(default=0)
    unidad=models.ForeignKey(Unidad_Medida, verbose_name='Unidad de Medida')
    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name='Material'
        verbose_name_plural='Materiales'
        ordering=["descripcion"]

class Area(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Area'
        verbose_name_plural='Areas'

class Persona(models.Model):
    nombre=models.CharField(max_length=100)
    area=models.ForeignKey(Area, verbose_name='Area donde trabaja')
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Persona'
        verbose_name_plural='Personas'



