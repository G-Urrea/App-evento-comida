#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()

import db
import sys
import codecs
import json

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Pa' que funque UTF-8
database = db.Datasaver('localhost', 'root', '', 'tarea2')
form = cgi.FieldStorage()
id  = form["id"].value
print('Content-type: text/html; charset=UTF-8')
print("")

map_list = database.get_map_list_info(id)
map_list_dict = {}
id_revisados = []
def buscar_fotos(id, lista):
    fotos = []
    for data in lista:
        if data[0]==id:
            fotos.append(data[5])
        else:
            break
    return fotos

for i in range(len(map_list)):
    dato = map_list[i]
    if dato[1] not in map_list_dict:
        comuna = dato[1]
        map_list_dict[dato[1]] = []
    if dato[0] not in id_revisados:
        photos = buscar_fotos(dato[0], map_list[i:])
        map_list_dict[dato[1]].append([dato[0],*dato[2:5], photos])
        id_revisados.append(dato[0])

data =  map_list_dict
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
inject = "<p style='text-align:center;font-weight:bold'>"+comuna+"</p>"
inject += "<table><tr><th>Enlace<th>dia-hora-inicio</th><th>Tipo de comida</th><th>Sector</th><th>Fotos</th></tr>"

for eventos in data[comuna]:
    inject += "<tr>"
    inject += "<td><a href='"+ "/cgi-bin/info_evento.py?id=" +str(eventos[0])+"'" +" target = '_blank' rel='noreferrer noopener'>Ver evento</a></td>";
    inject += "<td>"+str(eventos[1])+"</td>"
    inject += "<td>"+str(eventos[2])+"</td>"
    inject += "<td>"+str(eventos[3])+"</td>"
    inject += "<td><div class='container'>"
    fotos  = eventos[4]
    for foto in fotos:
        inject+= "<img src='/media/"+str(foto)+"'"+"style='width: 80px; height: 60px;'>"
    inject += "</div></td>"
    inject += "</tr>"

inject +=  "</table>"                   
                            
print(inject)