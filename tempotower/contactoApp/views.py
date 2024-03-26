from django.shortcuts import render,redirect
from .models import contactanos
from django.core.mail import EmailMessage


# Create your views here.


def contacto(request):
    formulatio_contacto= contactanos.objects.all()
    return render(request, "contacto.html", {'mi_formnulario':formulatio_contacto})

def registrarFormC(request):
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    mail=request.POST['txtMail']
    mensaje=request.POST['txtMensaje']

    Contactanos = contactanos.objects.create(nombre=nombre, apellido=apellido, mail=mail, mensaje=mensaje)

    email=EmailMessage("MENSAJE DESDE TU PAGINA WEB TEMPOTOWER.COM",
    "El usuario con nombre {} {} con la direccion de correo {} te dejo el siguiente mensaje:\n\n {}".format(nombre,apellido,mail,mensaje),"",
    ["yoangelfc@gmail.com"],reply_to=[mail])

    try:
      email.send()
      return redirect('/contacto/?valido')
    except:
      return redirect('/contacto/?novalido')
   


def  buzon_sugerencia(request):
  return render(request, "buzon_sugerencia.html")


def dispobibilidad(request):
  return render(request, "dispobibilidad.html")

