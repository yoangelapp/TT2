from django.contrib import admin
from django.urls import path
from contactoApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contacto/', views.contacto, name='contacto' ),

    path('registrarFormularioC/', views.registrarFormC),

    path('buzonSugerencia/', views.buzon_sugerencia, name='buzon_sugerencia' ),

    path('disponibilidad/', views.dispobibilidad, name='disponibilidad' ),
    

    
]