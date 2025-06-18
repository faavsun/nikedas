const tallaButtons = document.querySelectorAll('.talla-btn');
const agregarCarritoBtn = document.querySelector('.agregar-carrito-btn');
const tallaSeleccionadaInput = document.querySelector('#talla-seleccionada');
let tallaSeleccionada = null;

tallaButtons.forEach(button => {
    button.addEventListener('click', function () {
        // Desactivar el botón de talla previamente seleccionado
        if (tallaSeleccionada) {
            tallaSeleccionada.classList.remove('btn-dark');
            tallaSeleccionada.classList.add('btn-outline-secondary');
        }

        // Activar el botón de talla seleccionado
        this.classList.remove('btn-outline-secondary');
        this.classList.add('btn-dark');
        tallaSeleccionada = this; // Actualizar la talla seleccionada

        // Actualizar el valor del input oculto con la talla seleccionada
        tallaSeleccionadaInput.value = this.getAttribute('data-talla');

        // Habilitar el botón de agregar al carrito una vez seleccionada la talla
        agregarCarritoBtn.disabled = false;
    });
});

