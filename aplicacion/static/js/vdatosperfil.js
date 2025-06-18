window.addEventListener('load', () => {

    const form = document.getElementById("formulario");
    const mensajeError = document.getElementById("mensajeError");

    form.addEventListener('submit', e => {
        e.preventDefault();
        validarFormulario();
    });

    function validarFormulario() {
        
        // Declaramos variables para comenzar las validaciones
        const mailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        const telefonoFormat = /^9\d{8}$/;
        
        const nombre = document.getElementById("id_nombre")
        const apellidos = document.getElementById("id_apellido")
        const telefono = document.getElementById("id_telefono")
        const correo = document.getElementById("id_correo")
        
        
        // Reseteamos los errores
        mensajeError.innerHTML = "";
        document.querySelectorAll(".is-invalid").forEach(el => el.classList.remove("is-invalid"));

        //Validacion campos completos
        if (nombre === "" || apellidos === "" || telefono === "" || correo === "") {
            mensajeError.innerHTML += "Por favor, complete todos los campos.<br>";
        }

        //Validacion nombre
        if (nombre.value.trim().length < 2 || nombre.length > 50) {
            mensajeError.innerHTML += `Ingrese un nombre válido.<br>`;
            nombre.classList.add("is-invalid");
            return false;
        }

        //Validacion apellido
        if (apellidos.value.trim().length < 2 || apellidos.value.trim().length > 50) {
            mensajeError.innerHTML += `Ingrese un apellido válido.<br>`;
            apellidos.classList.add("is-invalid");
            return false;
        }

        //Validacion correo
        if (!mailFormat.test(correo.value.trim())) {
            mensajeError.innerHTML += `El correo no es valido.<br>`;
            correo.classList.add("is-invalid");
            return false;
        }

        //Validacion telefono solo 9 numeros
        if (!telefonoFormat.test(telefono.value.trim())) {
            mensajeError.innerHTML += `El telefono no es valido.<br>`;
            telefono.classList.add("is-invalid");
            return false;
        }

        //Submit del formulario en caso de pasar las validaciones
        form.submit();
    
    }
    
})