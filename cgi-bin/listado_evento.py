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
listado = database.get_event_list()
print('Content-type: text/html; charset=UTF-8')
print("")

with open("static/html/listado_evento.html", 'r', encoding='utf8') as template:
    inject = ''
    script = '''
    function myInit() {
        loadnav();
    }
    '''

    if len(listado)>0: 
        inject = '''
        <div id="listado">
        <div class="titulo negrita">Listado de Eventos</div>
        <table class="table table-dark table-hover">
            <thead>
                <tr>
                    <th scope="col">Fecha-Hora Inicio</th>
                    <th scope="col">Fecha-Hora Termino</th>
                    <th scope="col">Comuna</th>
                    <th scope="col">Sector</th>
                    <th scope="col">Tipo comida</th>
                    <th scope="col">Nombre Contacto</th>
                    <th scope="col">N° de fotos</th>
                </tr>
            </thead>
            <tbody id="listado-tabla-cuerpo">
            {0}
            </tbody>
        </table>
         </div>
        '''
        rows = ''
        for data in listado:
            jsfunc = f'''
            location.assign('/cgi-bin/info_evento.py?id={data[0]}');
            '''
            rows +=f'''
            <tr class="tr-clickable" onclick = "{jsfunc}">
            <td>{data[1]}</td>
            <td>{data[2]}</td>
            <td>{data[3]}</td>
            <td>{data[4]}</td>
            <td>{data[5]}</td>
            <td>{data[6]}</td>
            <td>{data[7]}</td>
            </tr>
            '''

        inject = inject.format(rows)
        script += '''
        let options = {
            numberPerPage:5, //Cantidad de datos por pagina
            pageCounter:true, //Contador de paginas, en cual estas, de cuantas paginas
        };

        paginate.init('.table',options);
        '''
    else:
        inject = '<div>No hay datos que mostrar</div>'
    s = '{0}'
    p = template.read()
    print(s.format(p.format(inject, script)))