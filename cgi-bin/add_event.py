#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

cgitb.enable()

import db
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Pa' que funque UTF-8
form = cgi.FieldStorage()
database = db.Datasaver('localhost', 'root', '', 'tarea2')
print('Content-type: text/html; charset=UTF-8')

#INSERT INTO evento 
# (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tipo)
#  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);

nombre = form["nombre"].value
email = form["nombre"].value
cel = form["celular"].value
redes = form["red-social"]
region = form["region"].value
comuna = form["comuna"].value
sector = form["sector"].value
dhi = form["dia-hora-inicio"].value
dht = form["dia-hora-termino"].value
tcomida = form["tipo-comida"].value
desc = form["descripcion-evento"].value
fotos =  form["foto-comida"]

id_comuna = database.get_comuna_id(region, comuna)

event_data = (id_comuna, sector, nombre, email, cel, dhi, dht, desc, tcomida)

database.save_event(event_data)

head = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Información recibida</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../css/menu.css">
    <link rel="stylesheet" href="../css/success.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ"
        crossorigin="anonymous"></script>

</head>
'''

navbar = '''
<body class="body">
    <div class="topnav" id="myTopnav">
        <a href="../portada.html" class="active">Portada</a>
        <a href="../nuevo_evento.html">Informar Evento</a>
        <a href="../listado_eventos.html">Listado de eventos</a>
        <a href="../estadisticas.html">Estadisticas</a>
        <a href="javascript:void(0);" class="icon" onclick="myFunction()">
            <i class="fa fa-bars"></i>
        </a>
    </div>

'''


html = '''

    <div class="titulo negrita">Envío de información exitoso</div>
    <div class="main">
        Hemos recibido su información, muchas gracias y suerte en su emprendimiento
    </div>

    <button id="home-btn" class="boton" type="button" onclick="window.location('portada.html')">Volver a la portada</button>



'''
end = '''
    <script>
        function myFunction() {
            var x = document.getElementById("myTopnav");
            if (x.className === "topnav") {
                x.className += " responsive";
            } else {
                x.className = "topnav";
            }
        }
    </script>
</body>

</html>
'''

foo = f'''
<div>
<p>{redes}</p>
<p>{fotos}</p>
<p>Consulta Sql : {id_comuna}</p>
</div>
'''
print(head)
print(navbar)
print(foo)
print(end)