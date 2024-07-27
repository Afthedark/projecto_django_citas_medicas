from django.db import models
from citas import validators

class Paciente(models.Model):
    nombre = models.CharField(max_length=100, validators=[validators.validate_name])
    apellido = models.CharField(max_length=100, validators=[validators.validate_name])
    edad = models.IntegerField(validators=[validators.validate_age])
    direccion = models.CharField(max_length=200)
    
    
class Medico(models.Model):
    nombre=models.CharField(max_length=100, validators=[validators.validate_name])
    apellido=models.CharField(max_length=100, validators=[validators.validate_name])
    especialidad=models.CharField(max_length=100)

    
class Cita(models.Model):
    fecha = models.DateTimeField()
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE) #relacion uno a uno 
    
    
class Historial(models.Model):
    paciente=models.OneToOneField(Paciente, on_delete=models.CASCADE) #relacion uno a uno
    descripcion = models.TextField()
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    
    

    
    
    