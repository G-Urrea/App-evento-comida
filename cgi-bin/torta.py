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

types = database.get_types()
tipos = [p[0] for p in types]
valores = [p[1] for p in types]
data = [{'values': valores, 'labels': tipos, 'type':'pie'}]
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)