$(document).on('click', '.update-button', function (e) {
    e.preventDefault();
    var id = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: '{% url "carrello:cart_update" %}',
        data: {
            productid: $(this).data('index'),
            productqty: $('#select' + id + ' option').filter(':selected').val(),
            csrfmiddlewaretoken: "{{ csrf_token }}",
            action: 'post'
        },
        success: function (json) {
            document.getElementById("subtotal").innerHTML = json.prezzo;
            document.getElementById("cartqty").innerHTML = json.quantita;
        },
        error: function (xhr, errmsg, err) {
        }
    });
})