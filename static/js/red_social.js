let redes = ["Facebook" , "Twitter", "Instagram", "TikTok", "Otra"]

function mostrar_redes(){
    var select_red = "<option value='' selected='selected'>Seleccione red social</option>"
    for (const red of redes){
        select_red +="<option value='" + red+ "'>" + red+"</option>";
    }
    document.getElementById("red-social").innerHTML = select_red;
}