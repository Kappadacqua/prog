from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpRequest, HttpResponseRedirect

from shop_online.models import Prodotto


# Create your views here.

def aggiungi_carrello(request: HttpRequest):
    if not request.user.is_authenticated:
        return render(request, template_name="account/login_crispy.html")
    prodotto_id = request.POST.get("prodotto_id")
    prodotto_quantita = int(request.POST.get("prodotto_quantita"))

    if "carrello" not in request.session:
        request.session["carrello"] = {}
    if prodotto_id not in request.session["carrello"]:
        request.session["carrello"][prodotto_id] = 0

    request.session["carrello"][prodotto_id] += prodotto_quantita

    request.session.modified = True

    return HttpResponseRedirect(request.headers["Referer"])


def rimuovi_carrello(request: HttpRequest):
    prodotto_id = request.POST.get("prodotto_id")
    prodotto_quantita = int(request.POST.get("prodotto_quantita"))

    request.session["carrello"][prodotto_id] -= prodotto_quantita

    if request.session["carrello"][prodotto_id] <= 0:
        del request.session["carrello"][prodotto_id]

    request.session.modified = True

    return HttpResponseRedirect(request.headers["Referer"])



def visualizza_carrello(request: HttpRequest):
    if not request.user.is_authenticated:
        return render(request, template_name="account/login_crispy.html")

    if "carrello" not in request.session:
        request.session["carrello"] = {}

    ctx = {"prodotti": {Prodotto.objects.get(id=prodotto_id): prodotto_quantita for prodotto_id, prodotto_quantita in
                        request.session["carrello"].items()}}

    #ctx["subtotale"] = sum(float(prodotto.prezzo) * quantita for prodotto, quantita in ctx["prodotti"].items())
    #print(ctx["subtotale"])
    ctx["subtotale"]=request.session["subtotale"]= sum(float(prodotto.prezzo) * quantita for prodotto, quantita in ctx["prodotti"].items())

    return render(request, template_name="carrello/sommario2.html", context=ctx)


def paga_carrello(request: HttpRequest):
    ...
