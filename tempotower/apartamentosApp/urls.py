"""apartamentosAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apartamentosApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('apartamentos/', views.apartamentos, name='apartamentos' ),

    path('apartamentos/01/', views.apartamento01, name='apartamento01' ),

    path('apartamentos/habitaciones/', views.habitaciones, name='habitaciones' ),

    path('apartamentos/salas/', views.salas, name='salas' ),

    path('apartamentos/sociales/', views.sociales, name='sociales' ),

    path('apartamentos/cocinas/', views.cocinas, name='cocinas' ),
    
    path('apartamentos/gimnacio/', views.gimnacio, name='gimnacio' ),

    path('apartamentos/picuzzi/', views.picuzzi, name='picuzzi' ),

    path('apartamentos/estudio/', views.estudio, name='estudio' ),
]
