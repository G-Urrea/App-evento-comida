#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector
import hashlib

class Datasaver:

    def __init__(self, host, user, password, database):

        self.db = mysql.connector.connect(
        host = host, user =user,
        password = password, database = database
        )
        self.cursor = self.db.cursor(buffered = True)

    def get_regiones_comunas(self):
        query = ''' 
            SELECT distinct region.nombre, comuna.nombre 
            FROM region, comuna as nombre, comuna 
            WHERE region.id = comuna.region_id  
            ORDER BY region.nombre, comuna.nombre
            '''
        self.cursor.execute(query)
        return self.cursor.fecthall()
    
    def get_region(self, region):
        sql =f'''
        SELECT * FROM region WHERE nombre="{region}"
        '''
        self.cursor.execute(sql)
        region = self.cursor.fetchall()
        return region
    def get_comuna(self, comuna, region):
        sql = f'''
        SELECT comuna.nombre FROM comuna,
        (SELECT * FROM region WHERE region.nombre = "{region}") AS reg
        WHERE comuna.region_id=reg.id 
        AND comuna.nombre = "{comuna}";
        '''

        #sql = f'''
        #SELECT * FROM comuna WHERE nombre="{comuna}"
        #'''
        self.cursor.execute(sql)
        comuna = self.cursor.fetchall()
        return comuna
    def get_comuna_id(self, region, comuna):

        sql_id_region = f'''
        SELECT id FROM region WHERE nombre="{region}"
        '''
        self.cursor.execute(sql_id_region)
        id_region = self.cursor.fetchone()[0]

        sql_id_comuna = f'''
        SELECT id FROM comuna WHERE nombre="{comuna}" AND region_id="{id_region}"
        '''
        self.cursor.execute(sql_id_comuna)
        id_comuna = self.cursor.fetchone()[0]

        return id_comuna 

    def get_comuna_by_id(self, id):
        sql = f'''
        SELECT nombre FROM comuna WHERE id="{id}"
        '''
        self.cursor.execute(sql)
        comuna = self.cursor.fetchone()[0]
        return comuna

    def get_a_photo_by_id(self, id):
        sql = f'''
        SELECT ruta_archivo FROM foto 
        WHERE evento_id="{id}"
        '''
        self.cursor.execute(sql)
        archivo = self.cursor.fetchone()[0]
        return archivo
    
    def get_types(self):
        """
        Retorna el tipo de comida de los eventos y la cantidad de eventos para dicho tipo.
        """

        sql = '''
        SELECT tipo, COUNT(tipo) FROM `evento` GROUP BY evento.tipo;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
        

    def get_events_by_date(self):
        """
        Retorna la fecha y el números de eventos en dicha fecha
        """

        sql ='''
        SELECT fecha, COUNT(fecha) 
        FROM (SELECT CAST(dia_hora_inicio AS date) as fecha FROM evento AS f1) f1 
        GROUP BY fecha;
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data


    def get_month_hour(self):
        """
        Retorna el año-mes y hora-minuto de los eventos
        """

        sql ='''
        SELECT DATE_FORMAT(dia_hora_inicio, "%Y-%m") AS anno_mes,
        DATE_FORMAT(dia_hora_inicio,"%H:%i") AS hh_mm
        FROM evento
        ORDER BY DATE_FORMAT(dia_hora_inicio, "%Y-%m");
        '''

        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data


    def get_comuna_nfotos(self):
        """
        Retorna listado de comunas con eventos y el número de fotos para cada una
        """
        sql ='''
        SELECT comuna.nombre, COUNT(foto.id), comuna.id AS nfotos
        FROM evento, comuna, foto
        WHERE evento.comuna_id=comuna.id 
        AND foto.evento_id = evento.id
        GROUP BY comuna.nombre;
        '''

        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_map_list_info(self, id):
        """
        Retorna información relevante para el listado de eventos del mapa, entrega los siguientes datos:
        Id del evento, nombre de la comuna, fecha de inicio, tipo de comida, sector, ruta a fotos de comida
        """

        sql = f'''
        SELECT evento.id, comuna.nombre, DATE_FORMAT(evento.dia_hora_inicio,"%Y-%m-%d %H:%i") AS inicio,
        evento.tipo, evento.sector, foto.ruta_archivo
        FROM evento, foto, comuna
        WHERE evento.id = foto.evento_id
        AND comuna_id = comuna.id
        AND comuna_id = "{id}"
        ORDER BY evento.id;
        '''

        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def get_latest_events(self):
        sql = '''
        SELECT id, comuna_id, sector,
         dia_hora_inicio, dia_hora_termino, tipo 
         FROM evento ORDER BY id DESC LIMIT 5
        '''

        self.cursor.execute(sql)
        latest = self.cursor.fetchall()
        latest_list = []
        for event in latest:
            try:
                comuna = self.get_comuna_by_id(event[1])
                ruta_foto = self.get_a_photo_by_id(event[0])
                latest_list.append((ruta_foto, comuna , *event[2:]))
            except:
                return []
        return latest_list

    def get_event_list(self):
       # id, Fecha-Hora Inicio, Fecha-Hora Termino,Comuna, Sector, Tipo comida, Nombre Contacto, N° de fotos
        sql = '''
        SELECT evento.id, evento.dia_hora_inicio, evento.dia_hora_termino, comuna.nombre AS comuna,
        evento.sector, evento.tipo, evento.nombre, fotos.numero 
        FROM evento, comuna,
        (SELECT evento_id, COUNT(evento_id) AS numero 
        FROM foto GROUP BY evento_id) AS fotos
        WHERE evento.comuna_id = comuna.id AND evento.id= fotos.evento_id;
        '''
        self.cursor.execute(sql)
        event_query = self.cursor.fetchall()
        return event_query

    def get_event_info(self, id):
        sql = f'''
        SELECT evento.tipo, region.nombre as region, comuna.nombre as comuna, evento.sector,
        evento.dia_hora_inicio, evento.dia_hora_termino,
        evento.descripcion, evento.nombre, evento.email, evento.celular 
        FROM evento, region, comuna 
        WHERE evento.comuna_id = comuna.id AND comuna.region_id=region.id AND
        evento.id = "{id}";
        '''
        self.cursor.execute(sql)
        data = self.cursor.fetchone()

        sql = f'''
        SELECT nombre, identificador FROM red_social WHERE evento_id = "{id}";
        '''
        self.cursor.execute(sql)
        nets = self.cursor.fetchall()

        sql = f'''
        SELECT ruta_archivo FROM foto WHERE evento_id = "{id}";
        '''
        self.cursor.execute(sql)
        photos = self.cursor.fetchall()

        return (data, nets, photos)
    def save_event(self, event, nets, photos):
        
        sql = '''
            INSERT INTO 
            evento (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tipo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        self.cursor.execute(sql, event) # ejecuto la consulta
        self.db.commit() # modifico la base de datos

        id_evento = self.cursor.getlastrowid()

        sql = '''
        INSERT INTO red_social (nombre, identificador, evento_id) VALUES (%s, %s, %s);
        '''
        
        for pair in nets:
            self.cursor.execute(sql, (*pair, id_evento)) # ejecuto la consulta
            self.db.commit() # modifico la base de datos

        for photo in photos:
            filename = photo.filename
                
            # calculamos cuantos elementos existen y actualizamos el hash
            sql = "SELECT COUNT(id) FROM foto"
            self.cursor.execute(sql)
            total = self.cursor.fetchall()[0][0] + 1
            hash_archivo = str(total) + \
                            hashlib.sha256(filename.encode()).hexdigest()[0:30]

            # guardar el archivo
            file_path = 'media/' + hash_archivo
            open(file_path, 'wb').write(photo.file.read())
            sql = '''
            INSERT INTO foto (ruta_archivo, nombre_archivo, evento_id) VALUES (%s, %s, %s);
            '''
            self.cursor.execute(sql, (hash_archivo, filename, id_evento)) # ejecuto la consulta
            self.db.commit() # modifico la base de datos

