$(document).on('click', '.delete-button', function (e) {
    e.preventDefault();
    var id = $(this).data('index');
    $.ajax({
        type: 'POST',
        url: '{% url "carrello:cart_del.js" %}',
        data: {
            productid: $(this).data('index'),
            csrfmiddlewaretoken: "{{ csrf_token }}",
            action: 'post'
        },
        success: function (json) {
            $('.product-item[data-index="' + id + '"]').remove();
            document.getElementById("subtotal").innerHTML = json.prezzo;
            document.getElementById("cartqty").innerHTML = json.quantita;
        },
        error: function (xhr, errmsg, err) {
        }
    });
})