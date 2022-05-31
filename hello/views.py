from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

from .models import *

def index(request):
    return render(request, "index.html")

def Datos_generales(request):
    return render(request, "Datos_generales.html")

def Datos_medicos(request):
    return render(request, "Datos_medicos.html")

def Editar_Datos_generales(request):
    return render(request, "Editar_Datos_Generales.html")

def Editar_Datos_medicos(request):
    return render(request, "Editar_Datos_Medicos.html")

def Documentacion(request):
    return render(request, "Documentacion.html")

def Formato_inscripcion(request):
    return render(request, "Formato_inscripcion.html")

def Calificaciones(request):
    return render(request, "Calificaciones.html")

def Boletas(request):
    return render(request, "Boletas.html")

def Registro_tesis(request):
    return render(request, "Registro_tesis.html")

def Editar_registro_tesis(request):
    return render(request, "Editar_registro_de_tesis.html")
                                
def Liberacion_tesis(request):
    return render(request, "Liberacion_tesis.html")

def Carta_liberacion(request):
    return render(request, "Carta_liberacion.html")

def login(request):
    return render(request, "login.html")

def password_reset(request):
    return render(request, "password_reset.html")
