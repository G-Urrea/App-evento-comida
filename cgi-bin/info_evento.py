#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()

import db
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Pa' que funque UTF-8
database = db.Datasaver('localhost', 'root', '', 'tarea2')
dato = cgi.FieldStorage()
id  = dato["id"].value
data, redes, fotos = database.get_event_info(id)

print('Content-type: text/html; charset=UTF-8')
print("")

with open("static/html/info_evento.html", 'r', encoding='utf8') as template:
    script = '''
    function myInit() {
        loadnav();
    }
    var span = document.getElementsByClassName("close")[0];

    var modal = document.getElementById('myModal');
    var modalImg = document.getElementById('img01');

    span.onclick = function () {
            modal.style.display = "none";
        }

    function displayModal (src) {
            modal.style.display = 'block';
            modalImg.src = src;
    }
    '''
    social = ''
    for red in redes:
        social+=f'<p>{red[0]}:{red[1]}</p>'

    img =''
    for foto in fotos:
        img += f'''<img src="/media/{foto[0]}" class="display-imagenes" onclick="displayModal('/media/{foto[0]}')">'''

    s = '{0}'
    p = template.read()
    values = (*data, social, img, script)
    print(s.format(p.format(*values)))