from django.db import models

# Create your models here.

class contactanos(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=30)
    mail=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        texto="{0}"
        return texto.format(self.nombre)
