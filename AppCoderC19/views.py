
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


def inicio(req):
    #return HttpResponse('Vista de inicio')
    return render(req,"inicio.html",{})

def cursos(req):
    #return HttpResponse('Vista de cursos')
    return render(req,"cursos.html",{})

def profesores(req):
    #return HttpResponse('Vista de profesores')
     return render(req,"profesores.html",{})

def estudiantes(req):
    #return HttpResponse('Vista de estudiantes')
    return render(req,"estudiantes.html",{})
 
def entregables(req):
    #return HttpResponse('Vista entregable')
    return render(req,"entregables.html",{})