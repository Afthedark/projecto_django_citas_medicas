
from rest_framework import viewsets
from .models import Medico, Paciente, Cita
from .serializers import MedicoSerializer, PacienteSerializer, CitaSerializer, CreateCitaSerializer
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view

# ...
# MODEL VIEW SET
class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer 
    
class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    



# GENERIC API VIEW
class CitaCreateAndListView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


# CUSTOM API
#Crear un paciente api 
@api_view(['POST'])
def createPacienteCustomApi(request):
    cs = PacienteSerializer(data=request.data)
    if cs.is_valid():
        cs.save()
        return JsonResponse({"message": "Cita creada correctamente"}, status=201)
    else:
        return JsonResponse({"message": "Algo salió mal"}, status=400)




