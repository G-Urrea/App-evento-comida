import json
import db
import codecs

database = db.Datasaver('localhost', 'root', '', 'tarea2')
query = ''' 
SELECT distinct region.nombre, comuna.nombre 
FROM region, comuna as nombre, comuna 
WHERE region.id = comuna.region_id  
ORDER BY region.nombre, comuna.nombre
 '''
regiones = database.get_regiones_comunas()
data = {}
for pair in regiones:
    if pair[0] not in data:
        data[pair[0]] = [pair[1]]
    else:
        data[pair[0]].append(pair[1])
        

y = json.dumps(data, ensure_ascii=False).encode('utf8').decode('utf8')

with codecs.open("static/json/regiones.json", "w", "utf-8") as outfile:
    outfile.write(y)