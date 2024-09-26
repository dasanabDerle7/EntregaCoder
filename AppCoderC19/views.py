
from django.shortcuts import render
from AppCoderC19.models import Curso
from  django.http import HttpResponse
# Create your views here.


def insertaCurso(res, Nombre, Camada):
    
    nuevo_curso=Curso(nombre=Nombre, camada=Camada)
    nuevo_curso.save()
    return HttpResponse(f"""
                        <p>Curso: {nuevo_curso.nombre}  - Camada: {nuevo_curso.camada} creado exitosamente. </p>
                                              """)


def listarCurso(req):
    lista=Curso.objects.all()
    return render(req,"listaCurso.html", {"Lista_Cursos":lista})
