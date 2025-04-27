from django.shortcuts import render
from django.http import HttpResponse
from django.views import View #Importamos View para poder usar vistas basadas en clases

# Vistas basadas en FUNCIONES
def bienvenido (request):
    return HttpResponse('<p> bienvenido desde mi otra_aplicacion 🤞 </p>')

#verificar si un numero es par o impar
def es_par(request, numero):
    if numero % 2 == 0:
        return HttpResponse(f'El numero {numero} es PAR')
    else:
        return HttpResponse(f'El numero {numero} es IMAPR')

#Vistas asadas en clases
class SaludoVista(View): #herencia View
    def get(self, request, nombre):   #esta funcion def se denominaria metodo
        return HttpResponse(f'Hola {nombre} desde una CLASE ✌😉')

class EsParVista(View):
    def get(self, request, numero):
        if numero % 2 == 0:
            return HttpResponse(f'El numero {numero} es PAR')
        else:
            return HttpResponse(f'El numero {numero} es IMAPR')
        

        