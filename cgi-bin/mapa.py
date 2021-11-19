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

comuna_nfotos  = database.get_comuna_nfotos()

with open("static/json/chile.json", "r", encoding="utf-8") as file:
    jason = file.read()
    chile =  json.loads(jason)

dic = {}
for t in chile:
    dic[t['name']] = [float(t['lat']), float(t['lng'])]

location = []
for comuna in comuna_nfotos:
    try:
        ncomuna = comuna[0]
        location.append([comuna[2], dic[ncomuna], comuna[1]])
    except:
        pass
y = json.dumps(location, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)
