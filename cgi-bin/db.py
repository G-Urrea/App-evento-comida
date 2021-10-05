#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mysql.connector


class Datasaver:

    def __init__(self, host, user, password, database):

        self.db = mysql.connector.connect(
        host = host, user =user,
        password = password, database = database
        )
        self.cursor = self.db.cursor()

    def make_sql(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

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

    def save_event(self, data):
        sql = '''
            INSERT INTO 
            evento (comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tipo) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        '''
        self.cursor.execute(sql, data) # ejecuto la consulta
        self.db.commit() # modifico la base de datos

    def save_social(self, data):
        sql = '''
        INSERT INTO red_social (nombre, identificador, evento_id) VALUES (%s, %s, %s);
        '''
        self.cursor.execute(sql, data) # ejecuto la consulta
        self.db.commit() # modifico la base de datos
    
    def save_photo(self, data):
        sql = '''
        INSERT INTO foto (ruta_archivo, nombre_archivo, evento_id) VALUES (%s, %s, %s);
        '''
        self.cursor.execute(sql, data) # ejecuto la consulta
        self.db.commit() # modifico la base de datos