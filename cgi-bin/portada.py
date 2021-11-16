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
latest = database.get_latest_events()
print('Content-type: text/html; charset=UTF-8')
print("")

with open("static/html/portada.html", 'r', encoding='utf8') as template:
    s = '''{0}'''
    inject = ''
    if(len(latest)==0):
        inject = '<div class="center categorias">No se han informado eventos aún </div>'
    else:
        inject = '''
        <table class="center">
        <tr>
            <th scope="col">Fecha-Hora Inicio</th>
            <th scope="col">Fecha-Hora Termino</th>
            <th scope="col">Comuna</th>
            <th scope="col">Sector</th>
            <th scope="col">Tipo</th>
            <th scope="col">Foto</th>
        </tr>
        '''
        for event in latest:
            #foto, comuna, sector, dia_hora_inicio, dia_hora_termino, tipo 
            inject+=f'''
            <tr>
            <td>{event[3]}</td>
            <td>{event[4]}</td>
            <td> {event[1]} </td>
            <td> {event[2]} </td>
            <td>{event[5]}</td>
            <td><img src="/media/{event[0]}" ></td>
            </tr>
            '''
        inject+='</table>'

    scpt1 = '''
    <script>
        var mymap = L.map('map').setView([-33.4500000, -70.6666667], 4);
        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
        }).addTo(mymap);

        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                    let rsp = xmlhttp.responseText;
                    let ubications = JSON.parse(rsp);

                    for (let i=0; i<ubications.length; i++){
                        let marker = L.marker(ubications[i][1], {title: "N° Fotos ="+ubications[i][2]}).addTo(mymap);
                        marker.bindPopup(String(ubications[i][0]), {maxHeight:250, minWidth:570,maxWidth:660});
                        marker.on('click', onClick);

                        function onClick(e) {
                            var popup = e.target.getPopup();
                            let id = popup.getContent();
                            popup.setContent('Espere...')
                            var xmlhttp2 = new XMLHttpRequest();
                            xmlhttp2.onreadystatechange = function () {
                                if (this.readyState == 4 && this.status == 200) {
                                        let inner  = xmlhttp2.responseText;
                                        popup.setContent(inner);
                                        e.target.off('click', onClick);
                                }
                            }
                            xmlhttp2.open("GET", "/cgi-bin/mapa_info.py?id="+id, true);
                            xmlhttp2.send();
                        }
                    }
                }
          }
        xmlhttp.open("GET", "/cgi-bin/mapa.py", true);
        xmlhttp.send();
    </script>
    '''
    p = template.read()
    print(s.format(p.format(inject, scpt1)))
    
