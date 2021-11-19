let comidas = [
    "Al Paso", "Alemana", "Árabe", "Argentina", "Asiática", "Australiana", "Brasileña", "Café y Snacks", "Carnes",
    "Casera", "Chilena", "China", "Cocina de Autor", "Comida Rápida", "Completos",
    "Coreana", "Cubana", "Española", "Exótica", "Francesa", "Gringa", "Hamburguesa", "Helados", "India",
    "Internacional", "Italiana", "Latinoamericana", "Mediterránea", "Mexicana", "Nikkei",
    "Parrillada", "Peruana", "Pescados y mariscos", "Picoteos",
    "Pizzas", "Pollos y Pavos", "Saludable", "Sándwiches", "Suiza",
    "Japonesa", "Sushi", "Tapas", "Thai", "Vegana", "Vegetariana"
]

function getJSON(path) {
    return fetch(path).then(response => response.json());
}
function mostrar_comida(){
    var comidas;
    getJSON('/static/json/tipo_comida.json').then(data => {
    comidas =  data;
    var select_comida = "<option value='' selected='selected'>Seleccione un tipo de comida</option>"
    for (const comida of comidas){
        select_comida +="<option value='" + comida+ "'>" + comida+"</option>";
    }
    document.getElementById("tipo-comida").innerHTML = select_comida;
    })
}