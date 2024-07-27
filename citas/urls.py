from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"medicos", views.MedicosViewSet)
router.register(r"pacientes",views.PacientesViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('citas/createAndList', views.CitaCreateAndListView.as_view()),
    path('citas/create', views.createPacienteCustomApi),
]








