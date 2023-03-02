$(document).on('click', '#add-button', function (e) {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '{% url "carrello:cart_add" %}',
        data: {
            prodottoid: $('#add-button').val(),
            productqty: $('#select option:selected').text(),
            csrfmiddlewaretoken: "{{ csrf_token }}",
            action: 'post'
        },
        success: function (json) {
            document.getElementById('cartqty').innerHTML = json.qty
        },
        error: function (xhr, errmsg, err) {
        }
    });
})