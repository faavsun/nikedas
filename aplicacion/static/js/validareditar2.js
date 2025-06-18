document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const submitButton = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', function (e) {
        let valid = true;
        let errorMessage = '';

        // Validar campos del formulario principal
        const modelo = form.querySelector('#id_modelo');
        const precio = form.querySelector('#id_precio');

        if (modelo.value.length < 2) {
            valid = false;
            errorMessage += 'El modelo debe tener al menos 2 caracteres.\n';
        }

        if (precio.value <= 0) {
            valid = false;
            errorMessage += 'El precio debe ser un número positivo y mayor a cero.\n';
        }

        // Validar campos del formset de stock
        const tallas = form.querySelectorAll('input[name$="-talla"]');
        const cantidades = form.querySelectorAll('input[name$="-cantidad"]');

        tallas.forEach((talla, index) => {
            if (talla.value <= 0) {
                valid = false;
                errorMessage += `La talla en la fila ${index + 1} debe ser un número positivo y mayor a cero.\n`;
            }
        });

        cantidades.forEach((cantidad, index) => {
            if (cantidad.value <= 0) {
                valid = false;
                errorMessage += `La cantidad en la fila ${index + 1} debe ser un número positivo y mayor a cero.\n`;
            }
        });

        if (!valid) {
            e.preventDefault();
            alert(errorMessage);
        }
    });
});