#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()

import db
import sys
import codecs
import validar

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Pa' que funque UTF-8
form = cgi.FieldStorage()
database = db.Datasaver('localhost', 'root', '', 'tarea2')
print('Content-type: text/html; charset=UTF-8')
print("")


# Para cargar parametros opcionales
def carga(storage, parametro, value= False):
    try:
        if value:
            par = storage[parametro].value
        else:
            par = storage[parametro]
    except:
        par = ''
    return par

nombre = form["nombre"].value
email = form["email"].value
cel = form["celular"].value
region = form["region"].value
comuna = carga(form, "comuna", True)
dhi = form["dia-hora-inicio"].value
dht = form["dia-hora-termino"].value
tcomida = form["tipo-comida"].value
photos =  form["foto-comida"]

fotos = []
try:
    photos.value # Si tiene value, entonces es uno solo
    if photos.filename:
        fotos.append(photos)
except:
    for photo in photos:
        if photo.filename:
            fotos.append(photo)

# Carga de parametros opcionales
redes = ["Facebook" , "Twitter", "Instagram", "TikTok", "Otra"]
redes_form = []
for x in redes:
    p = carga(form, x, value=True)
    if p!='':
        redes_form.append((x, p))

sector = carga(form, "sector", True)
desc = carga(form, "descripcion-evento", True)

# Validación acá
pair = validar.validacion(nombre, email, cel, region, comuna, dhi, dht, tcomida, fotos, redes_form)

if pair[0]: # Todo bien, todo correcto
    id_comuna = database.get_comuna_id(region, comuna)

    event_data = (id_comuna, sector, nombre, email, cel, dhi, dht, desc, tcomida)
    database.save_event(event_data, redes_form, fotos)# Subir a bdd
    with open("static/html/success.html", 'r', encoding='utf8') as template:
        file = template.read()
        print(file)
else: # oh no D:
    with open("static/html/nuevo_evento_error.html", 'r', encoding='utf8') as template:
        s = '{0}'
        file = template.read()
        error = ''
        script1 ='''
        window.addEventListener("load", myInit, true);
        function myInit() {
            insertar_fechas();
            mostrar_comida();
            mostrar_regiones();
            mostrar_redes();
            loadnav();
            '''
        
        script2='''
        };
        function close_error(){
            let error = document.getElementById("error");
            error.style.display= "none";
        }
        function envio() {
            let valid = validar_campos();
            if (valid) {
                let confirmacion = document.getElementById("confirmacion");
                let close_btn = document.getElementById("close-button");
                let send_btn = document.getElementById("send-button");

                confirmacion.style.display = "block";
                close_btn.onclick = function () {
                    confirmacion.style.display = "none";
                }
                send_btn.onclick = function () {
                    let forma = document.forms["evento"];
                    forma.submit();
                }

            }
        }
        function agregaInput() {
            let nfiles = document.getElementsByName("foto-comida").length;
            if (nfiles < 5) {
                var inp = document.createElement("input");
                inp.type = "file";
                inp.className = "foto";
                inp.name = "foto-comida"
                document.getElementById("archivos").appendChild(inp);
            }
        };

        function añadir_red(red_seleccionada) {
            let red_social = document.getElementById(red_seleccionada);

            if (red_social == null  && red_seleccionada != "") {
                let entry = document.createElement("div");
                entry.className = "entrada";

                let caption = document.createElement("div");
                caption.className = "leyenda";
                caption.innerHTML = red_seleccionada;
                entry.appendChild(caption);

                let inp = document.createElement("input");
                inp.type = "text";
                inp.placeholder = "Ingrese su url/id de " + red_seleccionada;
                inp.id = red_seleccionada;
                inp.name = red_seleccionada;
                entry.appendChild(inp)

                document.getElementById("form-redes").appendChild(entry);
            }
        }

        '''
        inject = '''
        let name = document.getElementById('nombre');
        nombre.value = "{0}";
        let email = document.getElementById('email');
        email.value = "{1}";
        let celular = document.getElementById('celular');
        celular.value = "{2}";
        let redes_keys = {3};
        let redes_values = {4}
        let sector = document.getElementById('sector');
        sector.value = "{5}";
        let dhi = document.getElementById('dia-hora-inicio');
        let dht = document.getElementById('dia-hora-termino');
        dhi.value = "{6}";
        dht.value = "{7}";
        let desc =  document.getElementById('descripcion-evento');
        desc.value = "{8}";
        '''

        inject_redes = '''
        for (let i = 0; i<redes_keys.length; i++){
            añadir_red(redes_keys[i]);
            let temp = document.getElementById(redes_keys[i]);
            temp.value = redes_values[i];
            }
        '''

        redes_values = [x[1] for x in redes_form]
        redes_keys = [x[0] for x in redes_form]
        tup = (nombre, email, cel, redes_keys, redes_values, sector, dhi, dht, desc)
        inject = inject.format(*tup) +  inject_redes
        script = script1+inject+script2

        for tupla in pair[1]:
            if not tupla[0]:
                if type(tupla[1])==str:
                    error+='<p>{0}</p>'.format(tupla[1])
                else:
                    string = '</p><p>'.join(tupla[1])
                    error+='<p>{0}</p>'.format(string)
        print(s.format(file.format(error, script)))