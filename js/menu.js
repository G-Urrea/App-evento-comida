function loadnav(){
    let div = document.getElementById("menu");
    let inner='<a href="portada.html" class="active">Portada</a>'+
    '<a href="nuevo_evento.html">Informar Evento</a>'+
    '<a href="listado_eventos.html">Listado de eventos</a>'+
    '<a href="estadisticas.html">Estadisticas</a>'+
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