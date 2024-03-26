from django.shortcuts import render

# Create your views here.

def apartamentos(request):
    return render(request, "apartamentos.html")


def apartamento01(request):
    return render(request, "apartamento01.html" ) 

def habitaciones(request):
    return render(request, "habitaciones.html")

def salas(request):
    return render(request, "salas.html")

def sociales(request):
    return render(request, "sociales.html")

def cocinas(request):
    return render(request, "cocinas.html")

def gimnacio(request):
    return render(request, "gimnacio.html")

def picuzzi(request):
    return render(request, "picuzzi.html")

def estudio(request):
    return render(request, "estudio.html")
