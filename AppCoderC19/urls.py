from django.contrib import admin
from django.urls import path, include
from AppCoderC19.views import * ## puedo traer de a uno, o todos -- insertaCurso, listarCurso,profesores,estudiantes,cursos,entregables, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insertaCurso/<Nombre>/<Camada>', insertaCurso,name="insertaCurso"),
    path('profesores/', profesores ,name="profesores"), 
    path('estudiantes/', estudiantes,name="estudiantes"),  
    path('cursos/', cursos,name="cursos"),
    path('entregable/', entregables,name="entregable"), 
    path('', inicio,name="inicio"), 
    
]
