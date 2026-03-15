from django.shortcuts import render, redirect
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        fecha = request.POST['fecha']
        hora = request.POST['hora']

        Tarea.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha=fecha,
            hora=hora
        )

        return redirect('/')

    return render(request, 'crear.html')