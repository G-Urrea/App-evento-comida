var today = new Date();
var today_3hrs = new Date(String(today));
today_3hrs.setHours(today_3hrs.getHours() + 3);

var hoy = fecha_a_string(today);
var hoy_3hrs = fecha_a_string(today_3hrs);

function insertar_fechas() {
    document.getElementById("dia-hora-inicio").value = hoy;
    document.getElementById("dia-hora-termino").value = hoy_3hrs;
};

function fecha_a_string(date) {
    let dia = String(date.getDate()).padStart(2, '0');
    let mes = String(date.getMonth() + 1).padStart(2, '0');
    let año = String(date.getFullYear());

    let hora = String(date.getHours()).padStart(2, '0');
    let minuto = String(date.getMinutes()).padStart(2, '0');

    let fecha = [año, mes, dia].join('-');
    let tiempo = [hora, minuto].join(':');
    let string = fecha + " " + tiempo;
    return string;
};

function validar_fecha(fecha) {
    let formato_fecha = /^[0-9]{4}[-](0?[1-9]|1[0-2])[-](0?[1-9]|[1-2][0-9]|3[0-1])$/;
    if (!formato_fecha.test(fecha)) {
        return false;
    }
    fecha_separada = fecha.split('-');
    let yy = parseInt(fecha_separada[0]);
    let mm = parseInt(fecha_separada[1]);
    let dd = parseInt(fecha_separada[2]);
    let ListofDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if (mm == 1 || mm > 2) {
        if (dd > ListofDays[mm - 1]) {
            return false;
        }
    }
    else if (mm == 2) {
        let lyear = false;
        if ((!(yy % 4) && yy % 100) || !(yy % 400)) {
            lyear = true;
        }
        if ((lyear == false) && (dd >= 29)) {
            return false;
        }
        if ((lyear == true) && (dd > 29)) {
            return false;
        }
    }
    else {
        return false;
    }
    return true;
};

function validar_hora(hora) {
    let formato_hora = /^([0-1][0-9]|2[0-4]):([0-5][0-9])$/;
    return formato_hora.test(hora);
};

function validar_dia_hora(dia_hora_inicio, dia_hora_termino) {
    let inicio = dia_hora_inicio.split(/[ ]+/);
    let final = dia_hora_termino.split(/[ ]+/);
    let validez_inicio = (validar_fecha(inicio[0]) && validar_hora(inicio[1]));
    let validez_final = (validar_fecha(final[0]) && validar_hora(final[1]));

    if (dia_hora_inicio == "" || dia_hora_termino == "") {
        alert("Señale fechas de inicio y termino");
        return false;
    }
    if (!(validez_inicio && validez_final)) {
        alert("Formato de fecha inválido");
        return false;
    }

    fecha_inicio = new Date(dia_hora_inicio);
    fecha_final = new Date(dia_hora_termino);

    if (fecha_final < today) {
        alert("Indique una fecha adecuada para su evento");
        return false;
    }

    if (fecha_inicio > fecha_final) {
        alert("Su evento no puede terminar antes de empezar!");
        return false;
    }
    return true;
}


function validar_nombre(nombre) {
    let name_regex = /^[a-zA-Z ]+$/;

    if (nombre == "" || !name_regex.test(nombre)) {
        alert("Nombre no válido");
        return false;
    }
    if (nombre.length >= 200) {
        alert("Su nombre es demasiado largo");
        return false;
    }
    return true;
};

function validar_ubicacion(region, comuna) {
    if (region == "") {
        alert("Debes escoger región");
        return false;
    }
    if (comuna == "") {
        alert("Debes escoger comuna");
        return false;
    }
    return true;
};

function validar_campos() {

    let email_regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    let celular_regex = /[+56]?9[0-9]{8}$/;
    let formato_foto = /.jpg|.jfif|.png$/;

    let forma = document.forms["evento"];
    let nombre = forma["nombre"].value;
    let email = forma["email"].value;
    let region = forma["region"].value;
    let comuna = forma["comuna"].value;
    let sector = forma["sector"].value;
    let celular = forma["celular"].value;
    let redes = document.getElementsByName("red-social");
    let fecha_inicio = forma["dia-hora-inicio"].value;
    let fecha_final = forma["dia-hora-termino"].value;
    let comida = forma["tipo-comida"].value;
    let fotos = document.getElementsByName("foto-comida");
    let nfotos = 0;
    let nredes = 0;

    for (let j = 0; j < redes.length; j++) {
        if (redes[j].value != "") {
            nredes += 1;
        }
    }

    if (!validar_nombre(nombre)) {
        return false;
    }

    if (!email_regex.test(email)) {
        alert("Email debe seguir formato xx@xx.xx");
        return false;
    }

    if (celular!="" && !celular_regex.test(celular)) {
        alert("Celular debe seguir formato 9xxxxxxxx o +569xxxxxxxx");
        return false;
    }

    if (nredes > 5) {
        alert("Son demasiadas redes sociales (max 5)");
        return false;
    }

    if (!validar_ubicacion(region, comuna)) {
        return false;
    }
    if (sector.length > 100) {
        alert("Su sector excede el numero máximo de carácteres (100)")
        return false;
    }
    if (!validar_dia_hora(fecha_inicio, fecha_final)) {
        return false;
    }
    if (comida == "") {
        alert("Seleccione un tipo de comida");
        return false;
    }
    for (let i = 0; i < fotos.length; i++) {
        if (fotos[i].value != "") {
            if(formato_foto.test(fotos[i].value)){
                nfotos += 1;
            }
            else{
                alert("Sólo se aceptan los siguientes formatos de foto: jpg, jfif, png");
                return false;
            }
            
        }
    }
    if (nfotos < 1 || nfotos > 5) {
        alert("El número de fotos subido debe estar entre 1 y 5");
        return false;
    }
    return true;
};