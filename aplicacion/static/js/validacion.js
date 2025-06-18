// rutValidator.js
const Fn = {
    // Valida el rut con su cadena completa "XXXXXXXX-X"
    validaRut: function (rutCompleto) {
        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutCompleto))
            return false;
        var tmp = rutCompleto.split('-');
        var digv = tmp[1];
        var rut = tmp[0];
        if (digv == 'K') digv = 'k';
        return (Fn.dv(rut) == digv);
    },
    dv: function (T) {
        var M = 0, S = 1;
        for (; T; T = Math.floor(T / 10))
            S = (S + T % 10 * (9 - M++ % 6)) % 11;
        return S ? S - 1 : 'k';
    }
};

window.addEventListener('load', () => {
    console.log('validacion')

    const form = document.getElementById("formulario");
    const mensajeError = document.getElementById("mensajeError");

    form.addEventListener('submit', e => {
        e.preventDefault();
        validarFormulario();

        form.classList.add('was-validated');

        if (!validarFormulario()) {
            form.classList.remove('was-validated');
        }
    });

    function validarFormulario() {
        // Declaramos las regex para validar
        const mailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        const passFormat = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/; //1 numero, 1 mayuscula, 1 minuscula min 6 caracteres
        const telefonoFormat = /^9\d{8}$/;

        const rut = document.getElementById("id_rut")
        const nombre = document.getElementById("id_nombre")
        const apellidos = document.getElementById("id_apellido")
        const correo = document.getElementById("id_correo")
        const fecha_nacimiento = document.getElementById("id_fnac")
        const password = document.getElementById("id_password1")
        const confirm_password = document.getElementById("id_password2")
        const telefono = document.getElementById("id_telefono")

        const direccion = document.getElementById("id_calle")
        const depto = document.getElementById("id_detalle")
        const region = document.getElementById("id_region")
        const comuna = document.getElementById("id_comuna")

        // Reseteamos los errores
        mensajeError.innerHTML = "";

        //Validacion nombre
        if (nombre.value.trim().length < 2 || nombre.value.trim().length > 50) {
            mensajeError.innerHTML += `El nombre es muy corto.`;
            nombre.classList.add("is-invalid");
            return false;
        }

        //Validacion apellido
        if (apellidos.value.trim().length < 2 || apellidos.value.trim().length > 50) {
            mensajeError.innerHTML += `El apellido es muy corto.`;
            apellidos.classList.add("is-invalid");
            return false;
        }

        if (!Fn.validaRut(rut.value.trim())) {
            mensajeError.innerHTML += `El RUT no es válido. Sin puntos y con guion.`;
            rut.classList.add("is-invalid");
            return false;
        }

        //Validacion fecha de nacimiento
        const fechaHoy = new Date();
        const fechaNacimiento = new Date(fecha_nacimiento.value.trim());

        //Verificamos que exista la fecha
        if (!fecha_nacimiento) {
            mensajeError.innerHTML += `Por favor, seleccione su fecha de nacimiento.`;
            fecha_nacimiento.classList.add("is-invalid");
            return false;
        }
        //Verificamos que no sea posterior a la fecha de hoy
        if (fechaNacimiento > fechaHoy) {
            mensajeError.innerHTML += `La fecha de nacimiento debe ser válida.`;
            fecha_nacimiento.classList.add("is-invalid");
            return false;
        }

        //Validacion correo
        if (!mailFormat.test(correo.value.trim())) {
            mensajeError.innerHTML += `El correo no es válido.`;
            correo.classList.add("is-invalid");
            return false;
        }

        //Validacion telefono solo 9 numeros
        if (!telefonoFormat.test(telefono.value.trim())) {
            mensajeError.innerHTML += `El teléfono no es válido. Formato: 912345678`;
            telefono.classList.add("is-invalid");
            return false;
        }

        //Validacion password segura
        if (password.value.trim().length < 6 || password.value.trim().length > 50) {
            mensajeError.innerHTML += `La contraseña debe tener al menos 6 caracteres y maximo 50`;
            password.classList.add("is-invalid");
            return false;
        }

        if (!passFormat.test(password.value.trim())) {
            mensajeError.innerHTML += `La contraseña debe tener al menos un numero, una mayuscula y una minuscula`;
            password.classList.add("is-invalid");
            return false;
        }

        //Validacion passwords coincidan
        if (password.value.trim() !== confirm_password.value.trim()) {
            mensajeError.innerHTML += `Las contraseñas no coinciden.`;
            password.classList.add("is-invalid");
            confirm_password.classList.add("is-invalid");
            return false;
        }


        if (direccion.value.trim().length < 4 || direccion.value.trim().length > 50) {
            mensajeError.innerHTML += `Ingrese una dirección valida.`
            direccion.classList.add("is-invalid");
            return false;
        }

        if (region.value.trim() === "") {
            mensajeError.innerHTML += "Por favor, seleccione una region";
            region.classList.add("is-invalid");
        }

        if (comuna.value.trim() === "") {
            mensajeError.innerHTML += "Por favor, seleccione una comuna";
            comuna.classList.add("is-invalid");
        }

        //Submit del formulario en caso de pasar las validaciones
        form.submit();
    }
})