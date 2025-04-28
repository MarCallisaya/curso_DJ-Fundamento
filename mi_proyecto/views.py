from django.shortcuts import render

def inicio(request):
    return render(request, 'mi_aplicacion/index.html')