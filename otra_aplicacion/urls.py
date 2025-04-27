from django.urls import path
from . import views    #El puntito hace referencia a la carpeta raiz (mi_aplicacion)
from .views import SaludoVista, EsParVista #del archivo views importando la clase, para que funciones la vista clase

urlpatterns = [
    path('bienvenida/',views.bienvenido), #registrando la ruta para la vista Hola mundo
    path('verificar/<int:numero>/',views.es_par),
    path('saludo/<str:nombre>/',SaludoVista.as_view()), #Vista basada en clases
    path('es_par/<int:numero>/',EsParVista.as_view()),
]
