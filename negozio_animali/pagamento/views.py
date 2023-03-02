import secrets
import string

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

from Negozio_animali_Balugani.settings import EMAIL_HOST_USER
from account.models import CustomUser
from ordini.models import Order, OrderItem
from shop_online.models import Prodotto


@login_required
def conferma_ordine(request):
    return render(request, template_name="pagamento/conferma_ordine.html")


def aggiungi_articoli_function(request):
    user_secret_key = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(25))
    user = get_object_or_404(CustomUser, username=request.user)
    subtotale=request.session["subtotale"]

    if Order.objects.filter(chiave_ordine =user_secret_key).exists():
        pass
    else:
        ordine = Order.objects.create(user=user, costo_totale=subtotale, stato_pagamento=True,chiave_ordine=user_secret_key)
        id_ordine = ordine.pk

        print(request.session["carrello"].items())

        for id_item,quantita in request.session["carrello"].items():
            item=Prodotto.objects.get(id=id_item)
            OrderItem.objects.create(ordine_id=id_ordine, prodotto=item,prezzo=item.prezzo,quantita=quantita)

    return "successo"

@login_required
def pagamento_effettuato(request):
    user = get_object_or_404(CustomUser, username=request.user)
    checkbox_mail = request.POST.get("mail")

    ordini = "".join((Prodotto.objects.get(id=prodotto_id).stampa_bene() + f" quantità = {prodotto_quantita}\n" for
                      prodotto_id, prodotto_quantita in request.session["carrello"].items()))

    if checkbox_mail:
        messaggio = f"Gentile {user.username}\n, ti ringraziamo per l'acquisto dei seguenti articoli:\n{ordini} L'articolo ti verrà spedito a casa in via {user.indirizzo}.\n Cordiali saluti, il negozio di animali"
        send_mail(subject=request.user, message=messaggio, from_email=EMAIL_HOST_USER, recipient_list=[user.email],
                  fail_silently=False)

    aggiungi_articoli_function(request)

    request.session["carrello"] = {}
    request.session.modified = True

    return render(request, template_name="pagamento/pagamento_effettuato.html", )
