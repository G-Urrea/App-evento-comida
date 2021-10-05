// return JSON data from any file path (asynchronous)
function getJSON(path) {
    return fetch(path).then(response => response.json());
}

var chile;
// load JSON data; then proceed
getJSON('../json/regiones.json').then(data => {
    // assign chile with data
    chile = data;
})

function mostrar_regiones() {
    var chile;
    // load JSON data; then proceed
    getJSON('../json/regiones.json').then(data => {
        // assign allQuestions with data
        chile = data;
        var regiones = Object.keys(chile)
        var select_regiones = "<option value='' selected='selected'>Seleccione una región</option>"
        for (var i = 0; i < regiones.length; ++i) {
            var nombre_region = regiones[i];
            select_regiones += "<option value='" + nombre_region + "'>" + nombre_region + "</option>";
        }
        document.getElementById("region").innerHTML = select_regiones;

    })
}

function mostrar_comunas(name) {
    var chile;
    // load JSON data; then proceed
    getJSON('../json/regiones.json').then(data => {
        // assign allQuestions with data
        chile = data;
        var comunas = chile[name]
        var select_comunas = "<option value='' selected='selected'>Seleccione una comuna</option>";

        for (var i = 0; i < comunas.length; ++i) {
            var nombre_comuna = comunas[i];
            select_comunas += "<option value='" + nombre_comuna + "'>" + nombre_comuna + "</option>";
        }

        document.getElementById("comuna").innerHTML = select_comunas;
    })
}
