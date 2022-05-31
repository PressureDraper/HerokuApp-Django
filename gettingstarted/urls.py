from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    #path("", hello.views.index),
    #path("", hello.views.page3),
    #path('welcome/', hello.views.page4),
    #path("db/", hello.views.db, name="db"),
    path('', hello.views.login, name="login"),
    path('password_reset',hello.views.password_reset, name='password_reset'),
    path('Bienvenida', hello.views.index, name="index"),
    path('Datos_generales', hello.views.Datos_generales, name="Datos_generales"),
    path('Datos_medicos/', hello.views.Datos_medicos, name="Datos_medicos"),
    path('Editar_Datos_generales/', hello.views.Editar_Datos_generales, name="Editar_Datos_generales"),
    path('Editar_Datos_medicos/', hello.views.Editar_Datos_medicos, name="Editar_Datos_medicos"),
    path('Documentacion/', hello.views.Documentacion, name="Documentacion"),
    path('Formato_inscripcion/', hello.views.Formato_inscripcion, name="Formato_inscripcion"),
    path('Calificaciones/', hello.views.Calificaciones, name="Calificaciones"),
    path('Boletas/', hello.views.Boletas, name="Boletas"),
    path('Registro_tesis/', hello.views.Registro_tesis, name="Registro_tesis"),
    path('Editar_registro_tesis',hello.views.Editar_registro_tesis, name="Editar_registro_tesis"),
    path('Liberacion_tesis/', hello.views.Liberacion_tesis, name="Liberacion_tesis"),
    path('Carta_liberacion/', hello.views.Carta_liberacion, name="Carta_liberacion"),
    path("admin/", admin.site.urls),
]
