from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import re
from django.http import FileResponse
import psycopg2
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
from django.views.generic import ListView, CreateView, TemplateView
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.db.models.functions import Cast, Coalesce
import numpy  as np
from django.utils.encoding import smart_str
from datetime import datetime

import numpy as np
import time
import _thread

import pylab as pl
from unicodedata import normalize


## De Reporteador

import io
from django.http import FileResponse
from reportlab.lib.pagesizes import A4
from django.core import serializers
from io import StringIO
from io import BytesIO
import itertools


#from datascience import *

from django.conf import settings
import os
from datetime import datetime
from datetime import date

from email.message import EmailMessage
import smtplib
from email import encoders


from .forms import solicitudesForm

# Create your views here.

def menuAcceso(request):
    print ("Ingreso al Menu Compras")
    context = {}

    # Sedes
    miConexion  = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432" , user="postgres", password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = 'SELECT ltrim(codreg_sede), nom_sede FROM public.imhotep_sedes'
    cur.execute(comando)
    print(comando)

    sedes = []

    for codreg_sede, nom_sede in cur.fetchall():
        sedes.append({'codreg_sede':codreg_sede, 'nom_sede' : nom_sede})
    miConexion.close()

    context['Sedes'] = sedes

    return render(request, "accesoPrincipal.html", context)


def validaAcceso(request):

    print ("Entre Validacion Acceso Compras")
    context = {}

    # Sedes
    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = 'SELECT id, codreg_sede, nom_sede FROM public.solicitud_sedesCompra'
    cur.execute(comando)
    print(comando)

    sedes = []

    for id,codreg_sede, nom_sede in cur.fetchall():
        sedes.append({'id' : id, 'codreg_sede': codreg_sede, 'nom_sede': nom_sede})
    miConexion.close()

    context['Sedes'] = sedes
    print ("Aqui estan las sedes")
    print (context['Sedes'])

    username = request.POST["username"]
    contrasena = request.POST["password"]
    sedeSeleccionada   = request.POST["seleccion2"]
    print ("sedeSeleccionada = " , sedeSeleccionada)
    print("username = ", username)
    print ("contrasena = ", contrasena)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada


    # Consigo Nombre de la sede

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                              password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT id,codreg_sede, nom_sede FROM public.solicitud_sedesCompra WHERE codreg_sede = '" + sedeSeleccionada + "'"
    #comando = 'SELECT codreg_sede, nom_sede FROM public."Administracion_imhotep_sedesreportes" where estadoReg=' + "'A'"
    cur.execute(comando)
    print(comando)

    nombreSede = []

    for id,codreg_sede, nom_sede in cur.fetchall():
        nombreSede.append({'id' : id,'codreg_sede': codreg_sede, 'nom_sede': nom_sede})

    miConexion.close()

    context['NombreSede'] = nombreSede[0]['nom_sede']

    # Validacion Usuario existente

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT num_identificacion, nom_usuario, clave_usuario, carg_usuario, sede_id  FROM public.solicitud_usuarios WHERE estadoReg = '" + "A' and num_identificacion = '" + username + "'"
    cur.execute(comando)
    print(comando)

    nombreUsuario = []

    for num_identificacion, nom_usuario, clave_usuario , carg_usuario,sede_id  in cur.fetchall():
        nombreUsuario.append({'num_identificacion': num_identificacion, 'nom_usuario': nom_usuario, 'clave_usuario' : clave_usuario, 'carg_usuario':carg_usuario,'sede_id':sede_id})

    miConexion.close()

    context['NombreUsuario'] = nombreUsuario[0]['nom_usuario']

    print ("Asi quedo el nombre del usuario",  context['NombreUsuario'])


    if nombreUsuario == []:

        context['Error'] = "Personal invalido y/o No Activo ! "
        print("Entre por personal No encontrado")

        return render(request, "accesoPrincipal.html", context)

        print("pase0")

    else:
        # Valido contraseña
        if nombreUsuario[0]['clave_usuario'] != contrasena:
            context['Error'] = "Contraseña invalida ! "
            return render(request, "accesoPrincipal.html", context)

        else:
            pass

            # Valido la Sede seleccinada

            miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                          password="BD_m3d1c4l")
            cur = miConexion.cursor()

            #comando = "SELECT num_identificacion  FROM public.solicitud_usuarios WHERE estadoReg='A' and num_identificacion = '" + username + "' and codreg_sede =  '"  + sedeSeleccionada + "'"
            comando = "SELECT num_identificacion,nom_sede  FROM public.solicitud_usuarios usu, public.solicitud_sedesCompra sedes WHERE usu.sede_id = sedes.id and usu.estadoReg='A' and usu.num_identificacion = '" + username + "' and sedes.codreg_sede =  '" + sedeSeleccionada + "'"
            print(comando)
            cur.execute(comando)

            permitido = []

            for num_identificacion, nom_sede in cur.fetchall():
                permitido.append({'num_identificacion': num_identificacion, 'nom_sede': nom_sede})

            miConexion.close()



            if permitido == []:

                context['Error'] = "Usuario no tiene autorizacion para la sede seleccionada y/o Reportes no asignados ! "
                return render(request, "accesoPrincipal.html", context)

            else:
                pass
                print("Paso Autenticacion")

    print("Asi quedo el nombre del usuario", context['NombreUsuario'])
    return render(request, "Reportes/cabeza.html", context)



def salir(request):
    print("Voy a salir Compras")

    context = {}
    # Sedes
    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()

    comando = 'SELECT codreg_sede, nom_sede FROM public."Administracion_imhotep_sedesreportes"'
    cur.execute(comando)
    print(comando)

    sedes = []

    for codreg_sede, nom_sede in cur.fetchall():
        sedes.append({'codreg_sede': codreg_sede, 'nom_sede': nom_sede})
    miConexion.close()

    context['Sedes'] = sedes
    print("Aqui estan las sedes")
    print(context['Sedes'])

    return render(request, "accesoPrincipal.html", context)


def Solicitudes(request , username, sedeSeleccionada, nombreUsuario, nombreSede):
    pass
    print ("Entre crear solicitudes");
    context = {}
    print("username = ", username)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    #context['solicitudesForm'] = solicitudesForm
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede

    print("SedeSeleccionada = ", sedeSeleccionada)

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")

    miConexion.set_client_encoding('LATIN1')
    cur = miConexion.cursor()
    cur.execute("set client_encoding='LATIN1';")
    comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    #Reemplazado
    #comando = "SELECT areas.codreg_area id ,areas.area  area FROM mae_areas areas, imhotep_sedes sedes WHERE areas.activo = 'S' and areas.sede = sedes.sede and sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    cur.execute(comando)
    print(comando)

    areas = []
    areas.append({'id': '', 'area': ''})

    for id, area in cur.fetchall():
        areas.append({'id': id, 'area': area})

    miConexion.close()

    context['Areas'] = areas



    # Combo descripcionescompra

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    cur = miConexion.cursor()

    comando = "SELECT t.id id, t.nombre  nombre FROM public.solicitud_descripcioncompra t where estadoReg='A'"
    cur.execute(comando)
    print(comando)

    descripcionescompra = []
    descripcionescompra.append({'id': '', 'nombre': ''})

    for id, nombre in cur.fetchall():
        descripcionescompra.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(descripcionescompra)

    context['Descripcionescompra'] = descripcionescompra

    # Fin combo descripcionescompra

    # Combo solicitud_tiposcompra

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    cur = miConexion.cursor()

    comando = "SELECT t.id id, t.nombre  nombre FROM public.solicitud_tiposcompra t where estadoReg='A'"
    cur.execute(comando)
    print(comando)

    tiposCompra = []
    tiposCompra.append({'id': '', 'nombre': ''})

    for id, nombre in cur.fetchall():
        tiposCompra.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(tiposCompra)

    context['TiposCompra'] = tiposCompra

    # Fin combo solicitud_presentacion

    # Combo solicitud_tiposcompra

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()

    comando = "SELECT t.id id, t.nombre  nombre FROM public.solicitud_presentacion t where estadoReg='A'"
    cur.execute(comando)
    print(comando)

    presentacion = []
    presentacion.append({'id': '', 'nombre': ''})

    for id, nombre in cur.fetchall():
        presentacion.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print(presentacion)

    context['Presentacion'] = presentacion

    # Fin combo solicitud_presentacion

    # Combo productos


    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    miConexion.set_client_encoding('LATIN1')
    cur = miConexion.cursor()
    cur.execute("set client_encoding='LATIN1';")

    comando = "SELECT t.codreg_articulo codreg_articulo,  translate(btrim(t.articulo::text),'óÓáÁéÉíÍúÚñÑ'::text,'oOaAeEiIuUnN'::text)      articulo   FROM public.mae_articulos t where activo='S' order by t.articulo"
    cur.execute(comando)
    print(comando)

    articulos = []
    articulos.append({'id': '', 'nombre': ''})

    for codreg_articulo, articulo in cur.fetchall():
        articulos.append({'codreg_articulo': codreg_articulo, 'articulo': articulo})

    miConexion.close()
    print(articulos)

    context['Articulos'] = articulos

    # Fin combo Productos


    return render(request, "Reportes/Solicitudes.html", context)

def guardarSolicitudes(request, username,sedeSeleccionada,nombreUsuario,fecha,nombreSede,area):
    pass
    if request.method == 'POST':
        if request.is_ajax and request.method == "POST":
            print("Entre Ajax")
            username = request.POST["username"]
            nombreSede = request.POST["nombreSede"]
            nombreUsuario = request.POST["nombreUsuario"]
            fecha = request.POST["fecha"]
            area = request.POST["area"]
            estadoReg='A'


            print ("Entre solicitudes Respuesta")
            print(username)
            print (nombreSede)
            print(nombreUsuario)
            print(fecha)
            print(area)

            if (area==""):
                return HttpResponse('Favor ingresar el Area de envio . ' )

            # Consigo el id del usuario :

            miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                          password="BD_m3d1c4l")
            cur = miConexion.cursor()
            comando = "SELECT id,num_identificacion, nom_usuario FROM public.solicitud_usuarios WHERE estadoReg = '" + "A' and num_identificacion = '" + username + "'"
            cur.execute(comando)
            print(comando)

            Usuario = []

            for id, num_identificacion, nom_usuario in cur.fetchall():
                Usuario.append(
                    {'id': id, 'num_identificacion': num_identificacion, 'nom_usuario': nom_usuario})

            miConexion.close()

            usuarioId = Usuario[0]['id']
            print(usuarioId)

            miConexiont = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                          password="BD_m3d1c4l")
            curt = miConexiont.cursor()

            comando = "INSERT INTO solicitud_solicitudes (fecha , estadoReg , area_id, usuarios_id) VALUES ('" + str(
                fecha) + "', '" + str(estadoReg) + "',  '" + str(area) + "', '" + str(
                usuarioId)  + "') RETURNING id;"

            print(comando)
            resultado = curt.execute(comando)
            print("resultado =", resultado)
            n = curt.rowcount
            print("Registros commit = ", n)

            miConexiont.commit()
            solicitudId = curt.fetchone()[0]

            print("solicitudId = ", solicitudId)
            miConexiont.close()

            print("El id de solicitud es  ", solicitudId)

            # Fin grabacion Solictud de Compra


            # Grabacion Solicitud
            print ("Entre a ver detalle solicitud")
            Envio = request.POST["jsonDefSol1"]

            print ("Envio1 = ", Envio)

            JsonDicEnvio = json.loads(Envio)
            print("Diccionario Envio1 = ", JsonDicEnvio)



            # Voy a iterar
            campo = {}
            item = 1

            for x in range(0, len(JsonDicEnvio)):
                print(JsonDicEnvio[x])
                campo1 = JsonDicEnvio[x]
                campo = json.loads(campo1)
                print(campo['descripcion'])
                print(campo['tipo'])
                print(campo['producto'])
                print(campo['presentacion'])
                print(campo['cantidad'])
                print(campo['justificacion'])
                descripcion =  campo['descripcion']
                tipo = campo['tipo']
                producto = campo['producto']
                presentacion = campo['presentacion']
                cantidad = campo['cantidad']
                justificacion = campo['justificacion']
                producto = campo['producto']

                # Aqui busco los id de cada cosa

                # Consigo Id username

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                              password="BD_m3d1c4l")
                cur = miConexion.cursor()
                comando = "SELECT id FROM public.solicitud_usuarios WHERE num_identificacion  = '" + username + "'"
                cur.execute(comando)
                print(comando)

                #usernameId = []
                usernameId = []

                for id in cur.fetchall():
                 usernameId.append({'id':id})
                   #usernameId['id'] = id

                miConexion.close()

                print ("V A L O R E S ")
                print (usernameId)
                print(usernameId[0])
                print(usernameId[0]['id'])
                #print(usernameId['id'])

                print("dato")
                for dato in usernameId:
                    print(dato)
                    print (dato['id'])
                    print(json.dumps(dato['id']))
                    usuario1 = json.dumps(dato['id'])

                print("usuario1 = ", usuario1)
                usuario1 = usuario1.replace('[','')
                usuario1 = usuario1.replace(']', '')
                print("usuario1 = ", usuario1)


                # Fin  Consigo Id username

                # Consigo Id descripcion

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                              password="BD_m3d1c4l")
                cur = miConexion.cursor()
                comando = "SELECT id FROM public.solicitud_descripcioncompra WHERE nombre  = '" + descripcion + "'"
                cur.execute(comando)
                print(comando)

                descripcionId = []

                for id in cur.fetchall():
                    descripcionId.append({'id': id})

                miConexion.close()

                print("dato")
                for dato in descripcionId:
                    print(dato)
                    print(dato['id'])
                    print(json.dumps(dato['id']))
                    descripcion1 = json.dumps(dato['id'])

                print("descripcionId = ", descripcionId)
                descripcion1 = descripcion1.replace('[', '')
                descripcion1 = descripcion1.replace(']', '')
                print("descripcion1 = ", descripcion1)

                # Fin  Consigo Id descripcion

                # Consigo Id tiposcomra

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                              password="BD_m3d1c4l")
                cur = miConexion.cursor()
                comando = "SELECT id FROM public.solicitud_tiposcompra WHERE nombre  = '" + tipo + "'"
                cur.execute(comando)
                print(comando)

                tipoId = []

                for id in cur.fetchall():
                    tipoId.append({'id': id})

                miConexion.close()

                print("dato")
                for dato in tipoId:
                    print(dato)
                    print(dato['id'])
                    print(json.dumps(dato['id']))
                    tipo1 = json.dumps(dato['id'])

                print("tipo1 = ", tipo1)
                tipo1 = tipo1.replace('[', '')
                tipo1 = tipo1.replace(']', '')
                print("tipo1 = ", tipo1)

                # Fin  Consigo Id tiposcomra

                # Consigo Id presentacion

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                              password="BD_m3d1c4l")
                cur = miConexion.cursor()
                comando = "SELECT id FROM public.solicitud_presentacion WHERE nombre  = '" + presentacion + "'"
                cur.execute(comando)
                print(comando)

                presentacionId = []

                for id in cur.fetchall():
                    presentacionId.append({'id': id})

                miConexion.close()

                print("dato")
                for dato in presentacionId:
                    print(dato)
                    print(dato['id'])
                    print(json.dumps(dato['id']))
                    presentacion1 = json.dumps(dato['id'])

                print("presentacion1 = ", presentacion1)
                presentacion1 = presentacion1.replace('[', '')
                presentacion1 = presentacion1.replace(']', '')

                print("presentacion1 DEFINITIVA = ", presentacion1)

                # Fin  Consigo Id presentacion

                ### Aqui fion busca Id pensientes

                miConexionu = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                              password="BD_m3d1c4l")
                curu = miConexionu.cursor()

                #comando = "INSERT INTO solicitud_solicitudesdetalle ( item ,  cantidad ,  justificacion ,  'especificacionesTecnicas' ,  'especificacionesAlmacen' ,  'especificacionesCompras' ,  estadoreg ,             descripcion_id, 'estadosAlmacen_id', 'estadosCompras_id', 'estadosSolicitud_id', 'estadosValidacion_id', solicitud_id, 'tiposCompra_id', 'usuarioResponsableValidacion_id', 'entregadoAlmacen', presentacion_id, 'solicitadoAlmacen' )         VALUES(" + str(item) + ", " + str(cantidad) + ", '" + str(justificacion) + "', '', '', '', 'A', " + descripcion1 + ", 1, 1, 1, 1, " + solicitudId + ", " + tipo1 + "," + usuario1 + ",0," + presentacion1+ ", 0)"
                comando = 'INSERT INTO solicitud_solicitudesdetalle ( item ,  cantidad ,  justificacion ,  "especificacionesTecnicas" ,  "especificacionesAlmacen" ,  "especificacionesCompras" ,  estadoreg ,             descripcion_id, "estadosAlmacen_id", "estadosCompras_id", "estadosSolicitud_id", "estadosValidacion_id", solicitud_id, "tiposCompra_id", "usuarioResponsableValidacion_id", "entregadoAlmacen", presentacion_id, "solicitadoAlmacen", producto)  VALUES(' + str(item) + ', ' + str(cantidad) + ',' + "'" + str(justificacion) + "'" + ",''," + "''" + ",'',"  + "'A'" + ','  + str(descripcion1) + ', 1, 1, 1, 1, ' + str(solicitudId) + ', ' + str(tipo1) + ',' + str(usuario1) + ',0,' + str(presentacion1) + ', 0,' + "'" + str(producto) + "'" +  '  )'
                print(comando)
                curu.execute(comando)
                miConexionu.commit()
                item=item+1
                miConexionu.close()

            # Fin Rutina Grabacion del detalle de la solicitud

    #Rutina envia correo electonico:


    #remitente = "adminbd@outlook.com"
    print("Entre correo1")
    #remitente = "adminbd@clinicamedical.com.co"
    #destinatario = "alberto_bernalf@yahoo.com.co"
    #mensaje = "Pruebas solicitudes"
    #email = EmailMessage()
    #print("Entre correo2")
    #email["From"] = remitente
    #email["To"] = destinatario
    #email["Subject"] = "Correo de prueba"
    #email.set_content(mensaje)
    #print("Entre correo3")
    #smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    #smtp = smtplib.SMTP("smtp.office365.com", port=587)
    #smtp.starttls()
    #print("Entre correo3.5")
    #smtp.login(remitente, "75AAbb??")
    #print("Entre correo4")
    #smtp.sendmail(remitente, destinatario, email.as_string())
    #print ("Correo Enviado")
    #smtp.quit()
    ## fin rutina correo electronico
    #print("salid de Correo Enviado")

    return HttpResponse('Solicitud creada No ' + str(solicitudId))



    #debe habes un POST


def ValidacionConsulta(request , username, sedeSeleccionada, nombreUsuario, nombreSede):
    pass
    print ("Entre a consulta solicitud a validar");
    context = {}

    print("username = ", username)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['solicitudesForm'] = solicitudesForm
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    #Reemplazado
    #comando = "SELECT areas.codreg_area id ,areas.area  area FROM mae_areas areas, imhotep_sedes sedes WHERE areas.activo = 'S' and areas.sede = sedes.sede and sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    cur.execute(comando)
    print(comando)

    areas = []

    for id, area in cur.fetchall():
        areas.append({'id': id, 'area': area})

    miConexion.close()

    context['Areas'] = areas

    return render(request, "Reportes/ValidacionConsulta.html", context)



#def ValidacionVerifica(request , username, sedeSeleccionada, nombreUsuario, nombreSede):
def ValidacionBusca(request):
    pass
    print ("Entre a validacionVerifica");
    context = {}
    username = request.POST["username"]
    nombreSede = request.POST["nombreSede"]
    nombreUsuario = request.POST["nombreUsuario"]
    sedeSeleccionada = request.POST["sedeSeleccionada"]
    solicitudId = request.POST["solicitudId"]

    print("username = ", username)
    print("sedeSeleccionada = ", sedeSeleccionada)
    print("solicitudId = ", solicitudId)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede
    context['SolicitudId'] = solicitudId

    # Buscamos la solicitud

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    #Pendiente de reemplazo
    comando = "SELECT sol.id id, sol.fecha fecha, sol.estadoReg estadoReg,sol.usuarios_id usuarioId , usu.nom_usuario nom_usuario, area.area nom_area, sede.nom_sede  nom_sede FROM public.solicitud_solicitudes sol ,public.solicitud_areas area , public.solicitud_sedesCompra sede, public.solicitud_usuarios usu WHERE sol.id = " + solicitudId + " AND area.id = sol.area_id and area.sede_id = sede.id and sol.usuarios_id = usu.id"
    cur.execute(comando)
    print(comando)

    solicitud = []

    for id, fecha,  estadoReg,usuarioId ,nom_usuario, nom_area, nom_sede in cur.fetchall():
        solicitud.append({'id': id, 'fecha': fecha,'estadoReg': estadoReg, 'usuarioId':usuarioId,'nom_usuario':nom_usuario,'nom_area':nom_area,'nom_sede' :nom_sede  })

    miConexion.close()
    print ("solicitud")
    print (solicitud)

    context['Solicitud'] = solicitud

    # Ahora SolicitudDetalle

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    #cur = miConexion.cursor()

    miConexion.set_client_encoding('LATIN1')
    cur = miConexion.cursor()
    cur.execute("set client_encoding='LATIN1';")

    #comando = "SELECT sol.id id, sol.fecha fecha, sol.estadoReg estadoReg,sol.usuarios_id usuarioId , usu.nom_usuario nom_usuario, area.area nom_area, sede.nom_sede  nom_sede FROM public.solicitud_solicitudes sol ,public.solicitud_areas area , public.solicitud_sedesCompra sede, public.solicitud_usuarios usu WHERE sol.id = " + solicitudId + " AND area.id = sol.area_id and area.sede_id = sede.id and sol.usuarios_id = usu.id"
    comando = 'SELECT sol.id id,sol.item item, sol.descripcion_id, des.nombre descripcion, tip.nombre tipo ,  art.articulo producto ,pres.nombre presentacion,sol.cantidad, sol.justificacion  , sol."especificacionesTecnicas" tec,usu.nom_usuario usuResp  , est.nombre estValidacion, sol."estadosValidacion_id" estadosValidacion_id  FROM public.solicitud_solicitudesDetalle sol , public.solicitud_descripcioncompra des, public.solicitud_tiposcompra tip, public.solicitud_presentacion pres, public.mae_articulos art    , public.solicitud_usuarios usu , public.solicitud_estadosvalidacion est  WHERE sol.solicitud_id = ' + solicitudId + ' AND des.id = sol.descripcion_id and tip.id = sol."tiposCompra_id" and pres.id = sol.presentacion_id and art.codreg_articulo = sol.producto and usu.id = sol."usuarioResponsableValidacion_id" and est.id = sol."estadosValidacion_id" ORDER BY sol.item'
    cur.execute(comando)
    print(comando)

    solicitudDetalle = []

    for id, item, descripcion_id, descripcion, tipo, producto, presentacion, cantidad, justificacion, tec, usuResp , estValidacion , estadosValidacion_id in cur.fetchall():
        solicitudDetalle.append(
            {'id': id, 'item':item , 'descripcion_id': descripcion_id, 'descripcion': descripcion, 'tipo': tipo, 'producto': producto,
             'presentacion': presentacion, 'cantidad': cantidad, 'justificacion': justificacion, 'tec':tec, 'usuResp':usuResp, 'estValidacion': estValidacion, 'estadosValidacion_id':estadosValidacion_id})

    miConexion.close()
    print("solicitudDetalle")
    print(solicitudDetalle)

    context['SolicitudDetalle'] = solicitudDetalle

    ## Voy a enviar estadosSolicitudes

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()

    comando = 'SELECT id,nombre FROM public.solicitud_estadosValidacion est'
    cur.execute(comando)
    print(comando)

    estadosValidacion = []

    for id, nombre in cur.fetchall():
        estadosValidacion.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print("estadosValidacion")
    print(estadosValidacion)

    context['EstadosValidacion'] = estadosValidacion


    ## Fin  a enviar estadosSolicitudes
    print ("solicitud = ", solicitud)
    # Fin SolicitudDetalle
    if (solicitud == []):
        print ("Entre por No existe")
        context['Error'] = 'Solicitud No Existe '
        miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                      password="BD_m3d1c4l")

        miConexion.set_client_encoding('LATIN1')
        cur = miConexion.cursor()
        cur.execute("set client_encoding='LATIN1';")
        comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
        cur.execute(comando)
        print(comando)
        areas = []
        areas.append({'id': '', 'area': ''})

        for id, area in cur.fetchall():
            areas.append({'id': id, 'area': area})

        miConexion.close()

        context['Areas'] = areas

        return render(request, "Reportes/ValidacionConsulta.html", context)
    else:
        return render(request, "Reportes/ValidacionTrae.html", context)


def GuardarValidacion(request):

    pass
    print ("Entre a validacionVerifica");
    context = {}
    #username = request.POST["username"]
    #nombreSede = request.POST["nombreSede"]
    #nombreUsuario = request.POST["nombreUsuario"]
    #sedeSeleccionada = request.POST["sedeSeleccionada"]
    #solicitudId = request.POST["solicitudId"]

    enviovalidacionDef = request.POST["enviovalidacionDef"]
    print ("enviovalidacionDef = ", enviovalidacionDef)

    JsonDicenviovalidacionDef = json.loads(enviovalidacionDef)
    print("Diccionario JsonDicenviovalidacionDef = ", JsonDicenviovalidacionDef)

    # Voy a iterar
    campo = {}
    item = 1

    for x in range(0, len(JsonDicenviovalidacionDef)):
                print(JsonDicenviovalidacionDef[x])
                campo1 = JsonDicenviovalidacionDef[x]
                campo = json.loads(campo1)
                print(campo['solicitudId'])
                print(campo['item'])
                print(campo['espTecnica'])
                print(campo['idEstado'])

                solicitudId =  campo['solicitudId']
                item = campo['item']
                espTecnica = campo['espTecnica']
                idEstado = campo['idEstado']

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                   password="BD_m3d1c4l")
                cur = miConexion.cursor()

                comando = 'UPDATE solicitud_solicitudesdetalle SET "especificacionesTecnicas" = ' + "'"  + str(espTecnica) + "'" + ', "estadosValidacion_id" = ' + str(idEstado) +  ' WHERE solicitud_id = ' + str(solicitudId) + ' and item = ' + str(item) + ' RETURNING id;'

                print(comando)
                resultado = cur.execute(comando)
                print("resultado =", resultado)
                n = cur.rowcount
                print("Registros commit = ", n)

                miConexion.commit()
                actualizado = cur.fetchone()[0]

                print("actualizado = ", actualizado)
                miConexion.close()


    return HttpResponse('Solicitud No: ' + solicitudId + ' Validada')

def AlmacenConsulta(request , username, sedeSeleccionada, nombreUsuario, nombreSede) :
    pass
    print("Entre a consulta Solicitudes a Almacen");
    context = {}

    print("username = ", username)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['solicitudesForm'] = solicitudesForm
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    # Reemplazado
    # comando = "SELECT areas.codreg_area id ,areas.area  area FROM mae_areas areas, imhotep_sedes sedes WHERE areas.activo = 'S' and areas.sede = sedes.sede and sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    cur.execute(comando)
    print(comando)

    areas = []

    for id, area in cur.fetchall():
        areas.append({'id': id, 'area': area})

    miConexion.close()

    context['Areas'] = areas

    return render(request, "Reportes/AlmacenConsulta.html", context)



def AlmacenBusca(request):
    pass

    print ("Entre a Almacen Busca");
    context = {}
    username = request.POST["username"]
    nombreSede = request.POST["nombreSede"]
    nombreUsuario = request.POST["nombreUsuario"]
    sedeSeleccionada = request.POST["sedeSeleccionada"]
    solicitudId = request.POST["solicitudId"]

    print("username = ", username)
    print("sedeSeleccionada = ", sedeSeleccionada)
    print("solicitudId = ", solicitudId)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede
    context['SolicitudId'] = solicitudId

    # Buscamos la solicitud

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    #Pendiente de reemplazo
    comando = "SELECT sol.id id, sol.fecha fecha, sol.estadoReg estadoReg,sol.usuarios_id usuarioId , usu.nom_usuario nom_usuario, area.area nom_area, sede.nom_sede  nom_sede FROM public.solicitud_solicitudes sol ,public.solicitud_areas area , public.solicitud_sedesCompra sede, public.solicitud_usuarios usu WHERE sol.id = " + solicitudId + " AND area.id = sol.area_id and area.sede_id = sede.id and sol.usuarios_id = usu.id"
    cur.execute(comando)
    print(comando)

    solicitud = []

    for id, fecha,  estadoReg,usuarioId ,nom_usuario, nom_area, nom_sede in cur.fetchall():
        solicitud.append({'id': id, 'fecha': fecha,'estadoReg': estadoReg, 'usuarioId':usuarioId,'nom_usuario':nom_usuario,'nom_area':nom_area,'nom_sede' :nom_sede  })

    miConexion.close()
    print ("solicitud")
    print (solicitud)

    context['Solicitud'] = solicitud

    # Ahora SolicitudDetalle

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    #cur = miConexion.cursor()

    miConexion.set_client_encoding('LATIN1')
    cur = miConexion.cursor()
    cur.execute("set client_encoding='LATIN1';")

    #comando = "SELECT sol.id id, sol.fecha fecha, sol.estadoReg estadoReg,sol.usuarios_id usuarioId , usu.nom_usuario nom_usuario, area.area nom_area, sede.nom_sede  nom_sede FROM public.solicitud_solicitudes sol ,public.solicitud_areas area , public.solicitud_sedesCompra sede, public.solicitud_usuarios usu WHERE sol.id = " + solicitudId + " AND area.id = sol.area_id and area.sede_id = sede.id and sol.usuarios_id = usu.id"
    comando = 'SELECT sol.id id,sol.item item, sol.descripcion_id, des.nombre descripcion, tip.nombre tipo ,  art.articulo producto ,pres.nombre presentacion,sol.cantidad, sol.justificacion  , sol."especificacionesTecnicas" tec,usu.nom_usuario usuResp  , est.nombre estValidacion, sol."estadosValidacion_id" estadosValidacion_id, sol."especificacionesAlmacen" especificacionesAlmacen, sol."estadosAlmacen_id" estadosAlmacen_id , sol."usuarioResponsableAlmacen_id"  usuarioResponsableAlmacen_id FROM public.solicitud_solicitudesDetalle sol , public.solicitud_descripcioncompra des, public.solicitud_tiposcompra tip, public.solicitud_presentacion pres, public.mae_articulos art    , public.solicitud_usuarios usu , public.solicitud_estadosvalidacion est  WHERE sol.solicitud_id = ' + solicitudId + ' AND des.id = sol.descripcion_id and tip.id = sol."tiposCompra_id" and pres.id = sol.presentacion_id and art.codreg_articulo = sol.producto and usu.id = sol."usuarioResponsableValidacion_id" and est.id = sol."estadosValidacion_id" ORDER BY sol.item'
    cur.execute(comando)
    print(comando)

    solicitudDetalle = []

    for id, item, descripcion_id, descripcion, tipo, producto, presentacion, cantidad, justificacion, tec, usuResp , estValidacion , estadosValidacion_id, especificacionesAlmacen, estadosAlmacen_id,usuarioResponsableAlmacen_id in cur.fetchall():
        solicitudDetalle.append(
            {'id': id, 'item':item , 'descripcion_id': descripcion_id, 'descripcion': descripcion, 'tipo': tipo, 'producto': producto,
             'presentacion': presentacion, 'cantidad': cantidad, 'justificacion': justificacion, 'tec':tec, 'usuResp':usuResp, 'estValidacion': estValidacion, 'estadosValidacion_id':estadosValidacion_id, 'especificacionesAlmacen':especificacionesAlmacen,'estadosAlmacen_id':estadosAlmacen_id,'usuarioResponsableAlmacen_id':usuarioResponsableAlmacen_id })

    miConexion.close()
    print("solicitudDetalle")
    print(solicitudDetalle)

    context['SolicitudDetalle'] = solicitudDetalle

    ## Voy a enviar estadosSolicitudes

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()

    comando = 'SELECT id,nombre FROM public.solicitud_estadosValidacion est'
    cur.execute(comando)
    print(comando)

    estadosValidacion = []

    for id, nombre in cur.fetchall():
        estadosValidacion.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print("estadosValidacion")
    print(estadosValidacion)

    context['EstadosValidacion'] = estadosValidacion


    ## Fin  a enviar estadosSolicitudes
    print ("solicitud = ", solicitud)
    # Fin SolicitudDetalle
    if (solicitud == []):
        print ("Entre por No existe")
        context['Error'] = 'Solicitud No Existe '
        miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                      password="BD_m3d1c4l")

        miConexion.set_client_encoding('LATIN1')
        cur = miConexion.cursor()
        cur.execute("set client_encoding='LATIN1';")
        comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
        cur.execute(comando)
        print(comando)
        areas = []
        areas.append({'id': '', 'area': ''})

        for id, area in cur.fetchall():
            areas.append({'id': id, 'area': area})

        miConexion.close()

        context['Areas'] = areas

        return render(request, "Reportes/AlmacenConsulta.html", context)
    else:
        return render(request, "Reportes/AlmacenTrae.html", context)


def GuardarAlmacen(request):

    pass
    print ("Entre a Almacen a Guardar");
    context = {}
    #username = request.POST["username"]
    #nombreSede = request.POST["nombreSede"]
    #nombreUsuario = request.POST["nombreUsuario"]
    #sedeSeleccionada = request.POST["sedeSeleccionada"]
    #solicitudId = request.POST["solicitudId"]

    envioAlmacenDef = request.POST["envioAlmacenDef"]
    print ("envioAlmacenDef = ", envioAlmacenDef)

    JsonDicenvioAlmacenDef = json.loads(envioAlmacenDef)
    print("Diccionario JsonDicenvioAlmacenDef = ", JsonDicenvioAlmacenDef)

    # Voy a iterar
    campo = {}
    item = 1

    for x in range(0, len(JsonDicenvioAlmacenDef)):
                print(JsonDicenvioAlmacenDef[x])
                campo1 = JsonDicenvioAlmacenDef[x]
                campo = json.loads(campo1)
                print(campo['solicitudId'])
                print(campo['item'])
                print(campo['espAlmacen'])
                print(campo['idEstadoAlm'])

                solicitudId =  campo['solicitudId']
                item = campo['item']
                espAlmacen = campo['espAlmacen']
                idEstadoAlm = campo['idEstadoAlm']

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                   password="BD_m3d1c4l")
                cur = miConexion.cursor()

                comando = 'UPDATE solicitud_solicitudesdetalle SET "especificacionesAlmacen" = ' + "'"  + str(espAlmacen) + "'" + ', "estadosAlmacen_id" = ' + str(idEstadoAlm) +  ' WHERE solicitud_id = ' + str(solicitudId) + ' and item = ' + str(item) + ' RETURNING id;'

                print(comando)
                resultado = cur.execute(comando)
                print("resultado =", resultado)
                n = cur.rowcount
                print("Registros commit = ", n)

                miConexion.commit()
                actualizado = cur.fetchone()[0]

                print("actualizado = ", actualizado)
                miConexion.close()


    return HttpResponse('Solicitud a Almacen No: ' + solicitudId + ' Actualizada')

## DESDE AQUI COMPRAS

def ComprasConsulta(request , username, sedeSeleccionada, nombreUsuario, nombreSede) :
    pass
    print("Entre a consulta Solicitudes a Compras");
    context = {}

    print("username = ", username)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['solicitudesForm'] = solicitudesForm
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    # Reemplazado
    # comando = "SELECT areas.codreg_area id ,areas.area  area FROM mae_areas areas, imhotep_sedes sedes WHERE areas.activo = 'S' and areas.sede = sedes.sede and sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
    cur.execute(comando)
    print(comando)

    areas = []

    for id, area in cur.fetchall():
        areas.append({'id': id, 'area': area})

    miConexion.close()

    context['Areas'] = areas

    return render(request, "Reportes/ComprasConsulta.html", context)



def ComprasBusca(request):
    pass

    print ("Entre a Compras Busca");
    context = {}
    username = request.POST["username"]
    nombreSede = request.POST["nombreSede"]
    nombreUsuario = request.POST["nombreUsuario"]
    sedeSeleccionada = request.POST["sedeSeleccionada"]
    solicitudId = request.POST["solicitudId"]

    print("username = ", username)
    print("sedeSeleccionada = ", sedeSeleccionada)
    print("solicitudId = ", solicitudId)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede
    context['SolicitudId'] = solicitudId

    # Buscamos la solicitud

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    #Pendiente de reemplazo
    comando = "SELECT sol.id id, sol.fecha fecha, sol.estadoReg estadoReg,sol.usuarios_id usuarioId , usu.nom_usuario nom_usuario, area.area nom_area, sede.nom_sede  nom_sede FROM public.solicitud_solicitudes sol ,public.solicitud_areas area , public.solicitud_sedesCompra sede, public.solicitud_usuarios usu WHERE sol.id = " + solicitudId + " AND area.id = sol.area_id and area.sede_id = sede.id and sol.usuarios_id = usu.id"
    cur.execute(comando)
    print(comando)

    solicitud = []

    for id, fecha,  estadoReg,usuarioId ,nom_usuario, nom_area, nom_sede in cur.fetchall():
        solicitud.append({'id': id, 'fecha': fecha,'estadoReg': estadoReg, 'usuarioId':usuarioId,'nom_usuario':nom_usuario,'nom_area':nom_area,'nom_sede' :nom_sede  })

    miConexion.close()
    print ("solicitud")
    print (solicitud)

    context['Solicitud'] = solicitud

    # Ahora SolicitudDetalle

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    #cur = miConexion.cursor()

    miConexion.set_client_encoding('LATIN1')
    cur = miConexion.cursor()
    cur.execute("set client_encoding='LATIN1';")

    #comando = "SELECT sol.id id, sol.fecha fecha, sol.estadoReg estadoReg,sol.usuarios_id usuarioId , usu.nom_usuario nom_usuario, area.area nom_area, sede.nom_sede  nom_sede FROM public.solicitud_solicitudes sol ,public.solicitud_areas area , public.solicitud_sedesCompra sede, public.solicitud_usuarios usu WHERE sol.id = " + solicitudId + " AND area.id = sol.area_id and area.sede_id = sede.id and sol.usuarios_id = usu.id"
    comando = 'SELECT sol.id id,sol.item item, sol.descripcion_id, des.nombre descripcion, tip.nombre tipo ,  art.articulo producto ,pres.nombre presentacion,sol.cantidad, sol.justificacion  , sol."especificacionesTecnicas" tec,usu.nom_usuario usuResp  , est.nombre estValidacion, sol."estadosValidacion_id" estadosValidacion_id, sol."especificacionesAlmacen" especificacionesAlmacen, sol."estadosAlmacen_id" estadosAlmacen_id , sol."usuarioResponsableAlmacen_id"  usuarioResponsableAlmacen_id,  sol."especificacionesCompras" especificacionesCompras, sol."estadosCompras_id" estadosCompras_id , sol."usuarioResponsableCompra_id"  usuarioResponsableCompra_id FROM public.solicitud_solicitudesDetalle sol , public.solicitud_descripcioncompra des, public.solicitud_tiposcompra tip, public.solicitud_presentacion pres, public.mae_articulos art    , public.solicitud_usuarios usu , public.solicitud_estadosvalidacion est  WHERE sol.solicitud_id = ' + solicitudId + ' AND des.id = sol.descripcion_id and tip.id = sol."tiposCompra_id" and pres.id = sol.presentacion_id and art.codreg_articulo = sol.producto and usu.id = sol."usuarioResponsableValidacion_id" and est.id = sol."estadosValidacion_id" ORDER BY sol.item'
    cur.execute(comando)
    print(comando)

    solicitudDetalle = []

    for id, item, descripcion_id, descripcion, tipo, producto, presentacion, cantidad, justificacion, tec, usuResp , estValidacion , estadosValidacion_id, especificacionesAlmacen, estadosAlmacen_id,usuarioResponsableAlmacen_id, especificacionesCompras, estadosCompras_id, usuarioResponsableCompra_id  in cur.fetchall():
        solicitudDetalle.append(
            {'id': id, 'item':item , 'descripcion_id': descripcion_id, 'descripcion': descripcion, 'tipo': tipo, 'producto': producto,
             'presentacion': presentacion, 'cantidad': cantidad, 'justificacion': justificacion, 'tec':tec, 'usuResp':usuResp, 'estValidacion': estValidacion, 'estadosValidacion_id':estadosValidacion_id, 'especificacionesAlmacen':especificacionesAlmacen,'estadosAlmacen_id':estadosAlmacen_id,'usuarioResponsableAlmacen_id':usuarioResponsableAlmacen_id,'especificacionesCompras':especificacionesCompras  ,'estadosCompras_id':estadosCompras_id , 'usuarioResponsableCompra_id':usuarioResponsableCompra_id})

    miConexion.close()
    print("solicitudDetalle")
    print(solicitudDetalle)

    context['SolicitudDetalle'] = solicitudDetalle

    ## Voy a enviar estadosSolicitudes

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()

    comando = 'SELECT id,nombre FROM public.solicitud_estadosValidacion est'
    cur.execute(comando)
    print(comando)

    estadosValidacion = []

    for id, nombre in cur.fetchall():
        estadosValidacion.append({'id': id, 'nombre': nombre})

    miConexion.close()
    print("estadosValidacion")
    print(estadosValidacion)

    context['EstadosValidacion'] = estadosValidacion


    ## Fin  a enviar estadosSolicitudes
    print ("solicitud = ", solicitud)
    # Fin SolicitudDetalle
    if (solicitud == []):
        print ("Entre por No existe")
        context['Error'] = 'Solicitud No Existe '
        miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                      password="BD_m3d1c4l")

        miConexion.set_client_encoding('LATIN1')
        cur = miConexion.cursor()
        cur.execute("set client_encoding='LATIN1';")
        comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "' order by areas.area"
        cur.execute(comando)
        print(comando)
        areas = []
        areas.append({'id': '', 'area': ''})

        for id, area in cur.fetchall():
            areas.append({'id': id, 'area': area})

        miConexion.close()

        context['Areas'] = areas

        return render(request, "Reportes/ComprasConsulta.html", context)
    else:
        return render(request, "Reportes/ComprasTrae.html", context)


def GuardarCompras(request):

    pass
    print ("Entre a Compras a Guardar");
    context = {}
    #username = request.POST["username"]
    #nombreSede = request.POST["nombreSede"]
    #nombreUsuario = request.POST["nombreUsuario"]
    #sedeSeleccionada = request.POST["sedeSeleccionada"]
    #solicitudId = request.POST["solicitudId"]

    envioComprasDef = request.POST["envioComprasDef"]
    print ("envioComprasDef = ", envioComprasDef)

    JsonDicenvioComprasDef = json.loads(envioComprasDef)
    print("Diccionario JsonDicenvioComprasDef = ", JsonDicenvioComprasDef)

    # Voy a iterar
    campo = {}
    item = 1

    for x in range(0, len(JsonDicenvioComprasDef)):
                print(JsonDicenvioComprasDef[x])
                campo1 = JsonDicenvioComprasDef[x]
                campo = json.loads(campo1)
                print(campo['solicitudId'])
                print(campo['item'])
                print(campo['espCompras'])
                print(campo['idEstadoComp'])

                solicitudId =  campo['solicitudId']
                item = campo['item']
                espCompras = campo['espCompras']
                idEstadoComp = campo['idEstadoComp']

                miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                   password="BD_m3d1c4l")
                cur = miConexion.cursor()

                comando = 'UPDATE solicitud_solicitudesdetalle SET "especificacionesCompras" = ' + "'"  + str(espCompras) + "'" + ', "estadosCompras_id" = ' + str(idEstadoComp) +  ' WHERE solicitud_id = ' + str(solicitudId) + ' and item = ' + str(item) + ' RETURNING id;'

                print(comando)
                resultado = cur.execute(comando)
                print("resultado =", resultado)
                n = cur.rowcount
                print("Registros commit = ", n)

                miConexion.commit()
                actualizado = cur.fetchone()[0]

                print("actualizado = ", actualizado)
                miConexion.close()


    return HttpResponse('Solicitud a Compras No: ' + solicitudId + ' Actualizada')



## HASTA AQUIP COMPRAS



def notifCompras(request , username, sedeSeleccionada, nombreUsuario, nombreSede):
    pass
    print("Entre crear solicitudes");
    context = {}
    pass
    print("Entre crear solicitudes");
    context = {}
    print("username = ", username)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['solicitudesForm'] = solicitudesForm
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "'  order by areas.area"
    cur.execute(comando)
    print(comando)

    areas = []

    for id, area in cur.fetchall():
        areas.append({'id': id, 'area': area})

    miConexion.close()

    context['Areas'] = areas

    return render(request, "Reportes/PantallaNotifCompras.html", context)






def ordenesDeCompra(request , username, sedeSeleccionada, nombreUsuario, nombreSede):
    pass
    print("Entre crear solicitudes");
    context = {}
    pass
    print("Entre crear solicitudes");
    context = {}
    print("username = ", username)
    context['Username'] = username
    context['SedeSeleccionada'] = sedeSeleccionada
    context['solicitudesForm'] = solicitudesForm
    context['NombreUsuario'] = nombreUsuario
    context['NombreSede'] = nombreSede

    miConexion = psycopg2.connect(host="192.168.0.237", database="bd_imhotep", port="5432", user="postgres",
                                  password="BD_m3d1c4l")
    cur = miConexion.cursor()
    comando = "SELECT areas.id id ,areas.area  area FROM public.solicitud_areas areas, public.solicitud_sedesCompra sedes WHERE areas.estadoreg = 'A' and areas.sede_id = sedes.id and  sedes.codreg_sede = '" + sedeSeleccionada + "'  order by areas.area"
    cur.execute(comando)
    print(comando)

    areas = []

    for id, area in cur.fetchall():
        areas.append({'id': id, 'area': area})

    miConexion.close()

    context['Areas'] = areas

    return render(request, "Reportes/PantallaOrdenesDeCompra.html", context)
