from rest_framework import serializers
from .models import Medico, Paciente, Cita

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class CreateCitaSerializer(serializers.Serializer):
    nombre=serializers.CharField(max_length=100)
    apellido=serializers.CharField(max_length=100)
    edad=serializers.IntegerField()
    direccion=serializers.CharField(max_length=100)


        