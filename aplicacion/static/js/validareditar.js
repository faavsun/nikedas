window.addEventListener('load', () => {
    const form = document.querySelector("form");
    const mensajeError = document.getElementById("mensajeError");

    form.addEventListener('submit', (e) => {
        if (!validarFormulario()) {
            e.preventDefault();
        }
    });

    function validarFormulario() {
        mensajeError.innerHTML = "";

        const modelo = document.getElementById("id_modelo").value.trim();
        const precio = document.getElementById("id_precio").value.trim();
        const talla = document.getElementById("id_talla").value.trim();
        const cantidad = document.getElementById("id_cantidad").value.trim();
        const imagen = document.getElementById("id_foto").value.trim();
        let errores = false;

        if (modelo === "" || modelo.length < 2) {
            mensajeError.innerHTML += "El modelo debe tener al menos 2 caracteres.<br>";
            errores = true;
        }

        if (isNaN(precio) || precio <= 0) {
            mensajeError.innerHTML += "El precio debe ser un número positivo y mayor a cero.<br>";
            errores = true;
        }

        if (isNaN(talla) || talla <= 0) {
            mensajeError.innerHTML += "La talla debe ser un número positivo y mayor a cero.<br>";
            errores = true;
        }

        if (isNaN(cantidad) || cantidad <= 0) {
            mensajeError.innerHTML += "La cantidad debe ser un número positivo y mayor a cero.<br>";
            errores = true;
        }

        const allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
        if (!allowedExtensions.exec(imagen)) {
            mensajeError.innerHTML += "Formato de imagen no válido. Solo se permiten archivos JPG, JPEG o PNG.<br>";
            errores = true;
        }

        return !errores;
    }
});
