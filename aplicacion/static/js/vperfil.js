window.addEventListener('load', () => {

    const form = document.getElementById("formulario");
    const mensajeError = document.getElementById("mensajeError");

    form.addEventListener('submit', e => {
        e.preventDefault(); // Aquí está la corrección
        validarFormulario();
    });

    function validarFormulario() {
        // Reseteamos los errores
        mensajeError.innerHTML = "";

        //Seleccionamos los elementos
        const calle = document.getElementById("calle").value.trim();
        const numero = document.getElementById("numero").value.trim();
        const depto = document.getElementById("depto").value.trim();
        const region = document.getElementById("region").value.trim();
        const comuna = document.getElementById("comuna").value.trim();
        //variables
        let warnings = ''


        //Validacion campos completos
        if (numero === "" || calle === "" || region === "" || comuna === "") {
            warnings += "Por favor, complete todos los campos<br>";
        }

        if (numero.length > 50 && numero.length < 5) {
            warnings += "Por favor, ingrese una direccion valida<br>";
        }

        if (numero.length > 7 && numero.length < 1) {
            warnings += "Por favor, ingrese el numero correcto<br>";
        }

        if (depto.length > 5) {
            warnings += "Por favor, ingrese el depto correcto<br>";
        }

        if(region !== "biobio" || region !== "metropolitana") {
            warnings += "Por favor, seleccione una region valida<br>"
        }

        if(comuna !== "concepcion" || comuna !== "talcahuano") {
            warnings += "Por favor, seleccione una comuna valida<br>"
        }


        

        // Mostrar los mensajes de advertencia
        mensajeError.innerHTML = warnings;

    }

})
