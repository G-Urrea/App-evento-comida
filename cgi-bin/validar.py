import re
import db
import json
import os
import filetype
import datetime
from datetime import datetime

    
def validar_nombre(nombre):
    """
    Válida un nombre. Retorna una tupla (bool, msg)
    """
    general_error = 'Nombre debe estar compuesto de letras'
    if len(nombre) > 200:
        return (False, 'Nombre : Nombre muy largo')
    elif len(nombre) == 0:
        return (False, 'Nombre : {0}'.format(general_error))
    else:
        only_letters = nombre.replace(" ", "")
        if not only_letters.isalpha():
            return (False, 'Nombre : {0}'.format(general_error))
    return (True, 'Nice')


def validar_email(email):
    email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(email_regex, email):
        return (True, 'NICE')
    else:
        return (False, 'Email : Email no válido, debe ser formato xx@xx.xx')


def validar_celular(celular):
    cel_regex = '[+56]?9[0-9]{8}$'
    if re.search(cel_regex, celular) or celular == "":
        return(True, 'Nice')
    else:
        return(False, 'Celular : Número no válido')


def validar_sector(sector):

    if len(sector) > 200:
        return(False, 'Sector : Nombre del sector es muy largo')
    else:
        return(True, 'NICE')


def validar_tcomida(tipo):
    with open('static/json/tipo_comida.json', encoding='utf8') as json_file:
        comidas = json.load(json_file)
    if tipo in comidas:
        return(True, 'Nice')
    else:
        return(False, 'Tipo de comida : El tipo recibido no corresponde con ninguno de los preestablecidos')

def validar_region(region):
    database = db.Datasaver('localhost', 'root', '', 'tarea2')
    if len(database.get_region(region))==0:
        return (False, 'Region : La región seleccionada no existe')
    else:
        return(True, 'NICE')

def validar_comuna(comuna, region):
    database = db.Datasaver('localhost', 'root', '', 'tarea2')
    if len(database.get_comuna(comuna, region))==0:
        return(False, 'Comuna : La comuna seleccionada no existe o no corresponde con la región seleccionada')
    else:
        return(True, 'Nice')

def validar_fechas(fecha_inicio, fecha_termino):
    err = []
    try:
        inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d %H:%M')
    except:        
        err.append('Dia-Hora inicio : Formato de fecha mal introducido')
    try:
        final = datetime.strptime(fecha_termino, '%Y-%m-%d %H:%M')
    
    except:
        err.append('Dia-Hora termino : Formato de fecha mal introducido')
    if len(err)>0:
        return(False, err)
    else:
        if final<inicio:
            return (False, 'Fecha-final : Fecha de termino es anterior a la fecha de inicio!')
        else:
            return (True, 'Nice')

def validar_fotos(fotos):

    if len(fotos)<1:
        return(False, 'Foto : Debías subir al menos una foto')
    if len(fotos)>5:
        return(False, 'Foto : Has subido demasiadas fotos (máx 5)')

    MAX_FILE_SIZE = 5000 * 1000  # 5.000 KB
    for photo in fotos:
        # vemos el tamaño en bytes
        size = os.fstat(photo.file.fileno()).st_size
        tipo_real = filetype.guess(photo.file)
        photo.file.seek(0, 0)  # devolver el puntero al inicio del archivo

        if size >= MAX_FILE_SIZE:
            return(False, 'Foto : Una de tus fotos es muy pesada (más de 5mb)')

        tipos_permitidos = ['image/png', 'image/jpeg']
        # (aquí serían imágenes, por ejemplo....)
        if tipo_real==None or (tipo_real.mime not in tipos_permitidos):
            return(False, 'Foto : Archivo no es una imagen aceptable (png o jpg)')
    return (True, 'Nice')

def validar_url(redes):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    id_regex = '^[a-zA-Z0-9_.]+$'
    fails = []

    for red in redes:
        if (not regex.search(red[1])) and (not re.search(id_regex, red[1])):
            fails.append('{} : Url (http(s)://direccion) o Id(Numeros,letras, "_" y ".") inválido'.format(red[0]))
    if len(fails)>0:
        return (False, fails)
    else:
        return(True, 'Nice')

def validacion(nombre, email, celular, region, comuna, dhi, dht, tcomida, fotos, redes):
    fine = True
    tuples = []
    tuples.append(validar_nombre(nombre))
    tuples.append(validar_email(email))
    tuples.append(validar_celular(celular))
    tuples.append(validar_region(region))
    tuples.append(validar_comuna(comuna, region))
    tuples.append(validar_fechas(dhi, dht))
    tuples.append(validar_tcomida(tcomida))
    tuples.append(validar_fotos(fotos))
    tuples.append(validar_url(redes))

    
    for tupla in tuples:
        fine = fine and tupla[0]

    return (fine, tuples)
