$(document).ready(function () {
    // Manejo de la petición a la API de Mindicador
    $.getJSON('https://mindicador.cl/api', function (data) {

        // Acceder al precio del producto desde el DOM
        const precioElemento = $("#precio-producto");
        const precioTexto = precioElemento.text().replace('$', '').replace(',', '').trim();
        const precio = parseFloat(precioTexto);

        // Cálculo del precio en dólares
        if (!isNaN(precio) && data.dolar) {
            const precioEnDolares = precio / data.dolar.valor;
            $("#dolar").text("USD $" + precioEnDolares.toFixed(2));
        } else {
            $("#dolar").text('Error al calcular el precio en dólares');
        }

    }).fail(function () {
        // Error al consumir la API
        console.log('Error al consumir la API');
        $("#dolar").text('Error al consumir la API');
    });
});
