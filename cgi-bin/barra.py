#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
cgitb.enable()

import db
import sys
import codecs
import json
from datetime import date, datetime

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # Pa' que funque UTF-8

database = db.Datasaver('localhost', 'root', '', 'tarea2')
print('Content-type: text/html; charset=UTF-8')
print("")

dates = database.get_month_hour()
months = []
morning = {}
noon = {}
afternoon = {}

t_6 = datetime.strptime('06:00', '%H:%M').time()
t_11 = datetime.strptime('11:00', '%H:%M').time()
t_15 = datetime.strptime('15:00', '%H:%M').time()

for pair in dates:
    if pair[0] not in months:
        months.append(pair[0])
        morning[pair[0]] = 0
        noon[pair[0]] = 0
        afternoon[pair[0]] = 0
    hora = datetime.strptime(pair[1], '%H:%M').time()
    
    if hora>=t_6 and hora<t_11:
        morning[pair[0]]+=1

    elif hora>=t_11 and hora<t_15:
        noon[pair[0]]+=1
    
    else:
        afternoon[pair[0]]+=1

months = [datetime.strftime(datetime.strptime(m, "%Y-%m"),'%B %Y') for m in months]
bar_morning = {'x':months, 'y':list(morning.values()),
 'name': 'Eventos que inician por la mañana', 'type':'bar'}

bar_noon = {'x':months, 'y':list(noon.values()),
 'name': 'Eventos que inician al mediodia', 'type':'bar'}

bar_afternoon = {'x':months, 'y':list(afternoon.values()),
 'name': 'Eventos que inician en la tarde', 'type':'bar'}

data = [bar_morning, bar_noon, bar_afternoon]
y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')
print(y)
