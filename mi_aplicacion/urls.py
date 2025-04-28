#from django.contrib import admin
from django.urls import path
from . import views    #El puntito hace referencia a la carpeta raiz (mi_aplicacion)

urlpatterns = [
    path('hola/',views.hola_mundo), #registrando la ruta para la vista Hola mundo
    path('patos/',views.pato),
    path('s/<str:nombre>/',views.saludar), #Registrando una vista con parametros
    path('plantilla/<str:nombre>/',views.usando_plantilla),
    path('productos/',views.lista_productos),
    path('',views.inicio),
    path('lista/',views.lista_estudiantes),
    path('contactos/',views.contactos,name='contactos'), #enrutar mediante botones menus name=contactos
    path('students/',views.students,name='students'),
    path('curso/<int:curso_id>/',views.detalle_curso,name='detalle_curso'),
    


]
