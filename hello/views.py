from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

from .models import *

# # Create your views here.
# def index(request):
#     #r = requests.get('https://httpbin.org/status/418')
#     return render(request, "vaccine.html")


# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, "db.html", {"greetings": greetings})

# def page3(request):
#     x = 'login.html'
#     if request.method == 'GET':
#         return render(request, x, {})
#     if request.method == 'POST':
#         if request.POST.get('enviar'):
#             #obtener los valores de user y passwd de los inputs
#             user = request.POST.get('user')
#             passwd = request.POST.get('passwd')
#             try:
#                 if testing.objects.get(username = user):
#                     #obtener el objeto completo de la consulta
#                     obj = testing.objects.get(username = user)
#                     #comparar valores del input con los de la base de datos
#                     if user.lower() == obj.username.lower() and passwd.lower() == obj.pwd.lower():
#                         #Se crea la cookie de sesión recuperando un dato
#                         request.session['cookie_session'] = request.POST.get('user', '')
#                         return redirect('/welcome')
#                     else:
#                         return redirect("/")
#             except:
#                 return redirect("/")
#         elif request.POST.get('registrar'):
#             user = request.POST.get('username')
#             passwd = request.POST.get('passwd')
#             obj = testing(username=user, pwd=passwd)
#             obj.save()
#             return redirect("/")

# def page4(request):
#     t = 'welcome.html'
#     #Se guarda la información de la cookie de sesión
#     data = request.session.get('cookie_session', '')
#     if data:
#         return render(request, t, {'name': data})
#     else:
#         return redirect("/")

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