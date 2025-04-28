from django.shortcuts import render
from django.http import HttpResponse #Importando http para renderisar respuesta sin HTML
from datetime import datetime

# Create your views here.
#Funciones 

def hola_mundo(request):
    return HttpResponse("<h1>Holaaa Estrellitas, el mundo les dice HOLA desde DJANGO</h1>")

def pato(request):
    return HttpResponse("Cuakkkk!!!! 🦆🦆🦆🦆🦆 ")

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}") #funciones que reciben argumentos ... f string

#Vista que usa la plantilla hola.html
def usando_plantilla(request, nombre):
    datos_persona = {
        'nombre': nombre,
        'edad':2,
        'fecha': datetime.now()
    }
    return render(request,'mi_aplicacion/hola.html',datos_persona) #return render(request,'DONDE',QUE)

def lista_productos(request):
    productos = [
        {'nombre':'Monitor','precio':1250},
        {'nombre':'Mouse','precio':120},
        {'nombre':'Teclado','precio':150},
        {'nombre':'Parlante','precio':50},
        {'nombre':'Audifonos','precio':190},
    ]
    return render(request,'mi_aplicacion/productos.html',{"productos":productos})

def inicio(request):
    datos_sitio = {
        'mensaje':'hola',
        'fecha': datetime.now()
    }
    return render(request,'mi_aplicacion/index.html',datos_sitio)


#TAREA 2
def lista_estudiantes(request):
    estudiantes = [
        {'nombre': 'Juan Pérez', 'ci': '12345678', 'celular': '76543210', 'fecha_nacimiento': '2005-04-15'},
        {'nombre': 'María López', 'ci': '87654321', 'celular': '71234567', 'fecha_nacimiento': '2006-11-20'},
        {'nombre': 'Carlos Mendoza', 'ci': '11223344', 'celular': '78901234', 'fecha_nacimiento': '2004-08-30'},
        {'nombre': 'Ana Torres', 'ci': '99887766', 'celular': '70123456', 'fecha_nacimiento': '2005-12-10'},
        {'nombre': 'Luis Gómez', 'ci': '44556677', 'celular': '70987654', 'fecha_nacimiento': '2003-07-05'},
        {'nombre': 'Verónica Salinas', 'ci': '55667788', 'celular': '70234567', 'fecha_nacimiento': '2006-01-22'},
        {'nombre': 'Pedro Rojas', 'ci': '33445566', 'celular': '70876543', 'fecha_nacimiento': '2005-10-03'},
        {'nombre': 'Laura Camacho', 'ci': '22334455', 'celular': '70432109', 'fecha_nacimiento': '2004-03-18'},
        {'nombre': 'Andrés Vaca', 'ci': '11221122', 'celular': '70654321', 'fecha_nacimiento': '2006-09-25'},
        {'nombre': 'Natalia Ruiz', 'ci': '88990011', 'celular': '70999988', 'fecha_nacimiento': '2005-06-14'},
    ]
    return render(request, 'mi_aplicacion/estudiantes.html', {"estudiantes": estudiantes})

def contactos(request):
    return render(request,'mi_aplicacion/contactos.html')

def students(request):
    return render(request,'mi_aplicacion/students.html')
