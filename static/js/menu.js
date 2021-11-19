function loadnav(){
    let div = document.getElementById("menu");
    let inner='<a href="/cgi-bin/portada.py" class="active">Portada</a>'+
    '<a href="/static/html/nuevo_evento.html">Informar Evento</a>'+
    '<a href="/cgi-bin/listado_evento.py">Listado de eventos</a>'+
    '<a href="/static/html/estadisticas.html">Estadisticas</a>'+
    '<a href="javascript:void(0);" class="icon" onclick=responsive()>'+
    '  <i class="fa fa-bars"></i>'+
    '</a>';
    div.innerHTML = inner;

}
function responsive() {
    var x = document.getElementById("menu");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }