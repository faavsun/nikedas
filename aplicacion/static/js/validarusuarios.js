window.addEventListener('load', () => {
    const form = document.getElementById("formulario_editar");

    form.addEventListener('submit', e => {
        e.preventDefault();
        validarFormulario();
    });

    function validarFormulario() {
        const nombre = document.getElementById("nombre").value.trim();
        const apellidos = document.getElementById("apellidos").value.trim();
        const direccion = document.getElementById("direccion").value.trim();
        const telefono = document.getElementById("telefono").value.trim();
        const correo = document.getElementById("email").value.trim();
        const fechaNacimiento = document.getElementById("fechaNacimiento").value.trim();

        const errorNombre = document.getElementById("errorNombre");
        const errorApellidos = document.getElementById("errorApellidos");
        const errorDireccion = document.getElementById("errorDireccion");
        const errorTelefono = document.getElementById("errorTelefono");
        const errorEmail = document.getElementById("errorEmail");
        const errorFechaNacimiento = document.getElementById("errorFechaNacimiento");

        errorNombre.innerHTML = "";
        errorApellidos.innerHTML = "";
        errorDireccion.innerHTML = "";
        errorTelefono.innerHTML = "";
        errorEmail.innerHTML = "";
        errorFechaNacimiento.innerHTML = "";

        let errores = false;

        if (nombre === "") {
            errorNombre.innerHTML = "Por favor, ingrese un nombre.<br>";
            errores = true;
        }

        if (apellidos === "") {
            errorApellidos.innerHTML = "Por favor, ingrese los apellidos.<br>";
            errores = true;
        }

        if (direccion === "") {
            errorDireccion.innerHTML = "Por favor, ingrese una dirección.<br>";
            errores = true;
        }

        if (telefono === "") {
            errorTelefono.innerHTML = "Por favor, ingrese un número de teléfono.<br>";
            errores = true;
        }

        if (correo === "") {
            errorEmail.innerHTML = "Por favor, ingrese un correo electrónico.<br>";
            errores = true;
        }

        if (fechaNacimiento === "") {
            errorFechaNacimiento.innerHTML = "Por favor, ingrese una fecha de nacimiento.<br>";
            errores = true;
        }

        if (errores) {
            return false;
        }

        form.submit(); // Envío del formulario si pasa todas las validaciones.
    }
});