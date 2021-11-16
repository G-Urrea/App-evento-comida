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
print('Content-type: text/html; charset=UTF-8')
print("")

types = database.get_events_by_date()
fechas = [str(p[0]) for p in types]
numero = [p[1] for p in types]
data = [{'x': fechas, 'y': numero, 'name':'Gráfico de línea'}]
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)