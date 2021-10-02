let database =
{
    "comida-chilena": {
        "fecha_inicio": "2021-10-07 12:00",
        "fecha_termino": "2021-10-07 14:00",
        "region": "Región Metropolitana de Valparaiso",
        "comuna": "La Florida",
        "sector": "Vicuña Mackenna",
        "tipo-comida": "Chilena",
        "nombre-contacto": "Juan Carlos Bodoque",
        "descripcion": "Porfavor comprenme empanadas, lo perdí todo en las apuestas :-(",
        "email": "JCB@31M.cl",
        "celular": "922326451",
        "redes": {"Instagram":"jcbodoque"},
        "fotos": ["images/empanadas.jpg"]
    },
    "comida-italiana": {
        "fecha_inicio": "2021-10-06 17:00",
        "fecha_termino": "2021-10-06 21:00",
        "region": "Región Metropolitana de Valparaiso",
        "comuna": "Santiago",
        "sector": "Plaza",
        "tipo-comida": "Italiana",
        "nombre-contacto": "Tonio Trussardi",
        "descripcion": "Mi comida les ayudará a llevar una vida más sana ;-)",
        "email": "Tonio@DIU.cl",
        "celular": "923826451",
        "redes": {"Twitter": "PJAM", "Facebook": "Trattoria"},
        "fotos": ["images/pizza.jpg", "images/pizza2.jpg"]
    },
    "comida-japonesa": {
        "fecha_inicio": "2021-10-07 17:00",
        "fecha_termino": "2021-10-07 21:00",
        "region": "Región Metropolitana de Valparaiso",
        "comuna": "Valparaiso",
        "sector": "Cerro Placeres",
        "tipo-comida": "Japonesa",
        "nombre-contacto": "Kanna Kamui",
        "descripcion": "Tendremos un onigiri muy rico y barato",
        "email": "kobayashi@gmail.cl",
        "celular": "923542451",
        "redes": "",
        "fotos": ["images/onigiri.jfif", "images/onigiri2.jpg", "images/onigiri3.jpg"]
    },
    "comida-china": {
        "fecha_inicio": "2021-10-06 17:00",
        "fecha_termino": "2021-10-06 21:00",
        "region": "Región Metropolitana de Santiago",
        "comuna": "Santiago",
        "sector": "10 de Julio",
        "tipo-comida": "China",
        "nombre-contacto": "Lee Sheng Shun",
        "descripcion": "Estaré vendiendo gyozas, a 100 pesos la unidad",
        "email": "Lee@sheenshung.cl",
        "celular": "923542341",
        "redes": {"Telegram":"@lsheng"},
        "fotos": ["images/gyoza.jpg", "images/gyoza2.jfif"]
    },
    "comida-india": {
        "fecha_inicio": "2021-10-11 17:00",
        "fecha_termino": "2021-10-11 21:00",
        "region": "Región Metropolitana de Santiago",
        "comuna": "Ñuñoa",
        "sector": "Estadio Nacional",
        "tipo-comida": "India",
        "nombre-contacto": "Muhammad Avdol",
        "descripcion": "En nombre de la fundación speedwagon estaremos vendiendo un delicioso pollo curry"
            + " para poder financiar una misión humanitaria a egipto.",
        "email": "Avdol@stardustcrusader.cl",
        "celular": "932452341",
        "redes": {"Twitter":"@mavdol", "Instagram":"mavdol"},
        "fotos": ["images/pollo-curry.jpg"]
    }
}// Simular una base de datos hasta tener el presupuesto para una de verdad :c

function insertar_datos(id) {
    /* Inserta la información de un evento para su visualización detallada */
    let info = database[id]
    document.getElementById("info-inicio").innerHTML = info["fecha_inicio"];
    document.getElementById("info-termino").innerHTML = info["fecha_termino"];
    document.getElementById("info-region").innerHTML = info["region"]
    document.getElementById("info-comuna").innerHTML = info["comuna"];
    document.getElementById("info-sector").innerHTML = info["sector"];
    document.getElementById("info-tipo").innerHTML = info["tipo-comida"];
    document.getElementById("info-contacto").innerHTML = info["nombre-contacto"];
    document.getElementById("info-descripcion").innerHTML = info["descripcion"];
    document.getElementById("info-email").innerHTML = info["email"];
    document.getElementById("info-nro").innerHTML = info["celular"];

    let redes = '';
    for (let key in info["redes"]){
        redes +='<p>'+ key + ' : '+ info["redes"][key]+'</p>';
    }
    document.getElementById("info-redes").innerHTML = redes;


    let ubicacion_imagenes = document.getElementById("info-imagenes");
    while (ubicacion_imagenes.childElementCount > 0) {
        let first = ubicacion_imagenes.firstChild;
        ubicacion_imagenes.removeChild(first);
    }

    for (let i = 0; i < info["fotos"].length; i++) {
        let img = document.createElement("img");
        let foto = info["fotos"][i];
        img.id = id + "-foto" + String(i);
        img.src = foto;
        img.className = "display-imagenes";
        ubicacion_imagenes.appendChild(img);

        let modal = document.getElementById("myModal");

        var modalImg = document.getElementById("img01");
        img.onclick = function () {
            modal.style.display = "block";
            modalImg.src = this.src;
        }

        var span = document.getElementsByClassName("close")[0];

        span.onclick = function () {
            modal.style.display = "none";
        }
    }

}

function inicializar_tabla() {
    let tabla = document.getElementById("listado-tabla-cuerpo");
    for (let key in database) {
        let db = database[key];
        let data = [db["fecha_inicio"], db["fecha_termino"], db["comuna"], db["sector"], db["tipo-comida"],
        db["nombre-contacto"], db["fotos"].length]
        let tr = document.createElement("tr");
        tr.className = "tr-clickable";
        tr.id = key;
        tr.onclick = function (){
            let tabla = document.getElementById("listado");
            let info = document.getElementById("info");

            insertar_datos(key);

            tabla.style.display = "none";
            info.style.display = "block";
        };
        for (let i in data) {
            tr.innerHTML += '<td>' + data[i] + '</td>'
        }
        tabla.appendChild(tr);
    }
}
