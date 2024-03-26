from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, "home.html")

def sobreNosotros(request):
    return render(request, "sobrenosotros.html") 

def apartamentos(request):
    return render(request, "services.html")

