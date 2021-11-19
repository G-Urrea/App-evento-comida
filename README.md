# App-evento-comida
Proyecto para el ramo CC5002 Desarrollo de Aplicaciones web. Consiste en una página web a través de la cuál se informan eventos de venta de comida

## Antes de iniciar la aplicación
Hay que tener MySQL y Apache. También hay que ejecutar los siguientes archivos sql de la carpeta database
- tarea2.sql
- region-comuna.sql

## Como iniciar la aplicación
Es necesario iniciar MySQL y Apache, luego de eso hay que meterse en la carpeta raíz de la aplicación y ejecutar el siguiente comando:
- python -m http.server --bind localhost --cgi 8000
