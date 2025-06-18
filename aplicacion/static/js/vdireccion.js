window.addEventListener('load', () => {

    const form = document.getElementById("formulario");


    form.addEventListener('submit', e => {
        e.preventDefault();
        validarFormulario();
    });

    function validarFormulario() {

        const direccion = document.getElementById("direccion").value.trim();
        const depto = document.getElementById("depto").value.trim();
        const region = document.getElementById("region").value.trim();
        const comuna = document.getElementById("comuna").value.trim();

        const errorDireccion = document.getElementById("errorDireccion");
        const errorDepto = document.getElementById("errorDepto");
        const errorRegion = document.getElementById("errorRegion");
        const errorComuna = document.getElementById("errorComuna");

        // Reseteamos los errores
        errorDireccion.innerHTML = "";
        errorRegion.innerHTML = "";
        errorComuna.innerHTML = "";



        if (direccion.length < 4 || direccion.length > 50) {
            errorDireccion.innerHTML = `Ingrese una direccion valida.`
            return false;
        }

        if (depto.length > 20) {
            errorDepto.innerHTML = "Ingrese un departamento o detalle valido."
            return false;
        }

        if (region === "") {
            errorRegion.innerHTML = "Por favor, seleccione una region.";
            return false;
        }

        if (comuna === "") {
            errorComuna.innerHTML = "Por favor, seleccione una region.";
            return false;
        }

        //Submit del formulario en caso de pasar las validaciones
        form.submit();
    }
})