from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas),
    path('crear/', views.crear_tarea),
]