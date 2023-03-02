from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from negozio_animali.account.models import CustomUser
from shop_online.forms import RecensioneForm
from shop_online.models import Prodotto, Animale, Categoria, Recensione


def pag_prod(request, slug):
    categorie = Categoria.ottieni_tutte_le_categorie()
    animali = Animale.ottieni_tutti_gli_animali()
    prodotto_specifico = get_object_or_404(Prodotto, slug=slug)
    ctx = {"animali": animali, "categorie": categorie, "prodotto": prodotto_specifico}
    return render(request, template_name="negozio_online/pagina_prodotto.html", context=ctx)


class ListaProdottiView2(ListView):
    model = Prodotto
    template_name = "negozio_online/indice.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        parametro = self.request.GET.get('id', None)
        print(parametro)
        if (parametro):
            return qs.filter(animale_id=parametro)
        else:
            return qs


def negozio_principale(request):
    categorie = Categoria.ottieni_tutte_le_categorie()


def ricerca_per_animale(request, animale):
    response = "lista_filtro_animale.html"
    temp = "negozio_online/indice.html"
    lista_animale = Prodotto.objects.filter(animale__nome__contains=animale)
    print(lista_animale)
    ctx = {"title": f"ricerca per f{animale}", "obj_list": lista_animale, "animale": animale}

    return render(request, template_name=temp, context=ctx)


class Barra_di_ricerca(ListView):
    model = Prodotto
    template_name = 'negozio_online/risultato_ricerca.html'
    context_object_name = 'risultati_trovati'

    def get_queryset(self):
        risultato = super(Barra_di_ricerca, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            print("a")
            # postresult = Prodotto.objects.filter(Q(a=query)|Q(prodotto_contains=query)|Q(prodotto_contains=query)|Q(prodotto_contains=query)|Q(prodotto_contains=query)|Q(prodotto_contains=query))
            # result = postresult
        else:
            result = None
        return result


def test(request):
    model = "prova.html"
    return render(request, template_name="negozio_online/../templates/prova.html")


class TuttiProdottiView(ListView):
    """vista di tutti i prodotti"""
    model = Prodotto
    template_name = "negozio_online/indice.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        parametro = self.request.GET.get('id', None)
        print(parametro)
        if (parametro):
            return qs.filter(animale_id=parametro)
        else:
            return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['titolo'] = "servo?"
        context["lista_per_pulsanti"] = Prodotto.get_animale_e_categorie_prodotti()
        print(Prodotto.get_animale_e_categorie_prodotti())
        return context


def NegozioPrincipale(request):
    categorie = Categoria.ottieni_tutte_le_categorie()
    animali = Animale.ottieni_tutti_gli_animali()
    prodotti = Prodotto.ottieni_tutti_i_prodotti()
    ctx = {"animali": animali, "categorie": categorie, "prodotti": prodotti}
    return render(request, template_name="negozio_online/indice.html", context=ctx)


def filtra_prodotti(request, **kwargs):
    categorie = Categoria.ottieni_tutte_le_categorie()
    animali = Animale.ottieni_tutti_gli_animali()

    slug_animale = kwargs.get("slug_animale", False)
    slug_categoria = kwargs.get("slug_categoria", False)

    prodotti = Prodotto.objects.all()

    if slug_animale:
        prodotti = prodotti.filter(animale__slug__contains=slug_animale)

    if slug_categoria:
        prodotti = prodotti.filter(categoria__slug__contains=slug_categoria)

    ctx = {"animali": animali, "categorie": categorie, "prodotti": prodotti,"slug_animale":slug_animale,"slug_categoria":slug_categoria}
    return render(request, template_name="negozio_online/indice.html", context=ctx)


def search(request):
    categorie = Categoria.ottieni_tutte_le_categorie()
    animali = Animale.ottieni_tutti_gli_animali()
    prodotti = Prodotto.ottieni_tutti_i_prodotti()
    if request.method == "GET":
        query = request.GET.get('cerca')
        if query == '':
            query = 'None'

        prodotti = Prodotto.objects.filter(
            Q(venditore__icontains=query) | Q(animale__nome__icontains=query) | Q(nome__icontains=query) | Q(categoria__nome__icontains=query))

    print(prodotti)
    ctx = {"animali": animali, "categorie": categorie, "prodotti": prodotti}
    return render(request, 'negozio_online/indice.html', context=ctx)
@login_required
def carrello(request,id_prodotto):
    pass


@login_required
def crea_recensione(request,slug):

    if request.method == 'POST':
        form = RecensioneForm(request.POST)

        if form.is_valid():
            prodotto = Prodotto.objects.get(slug=slug)
            user = CustomUser.objects.get(username=request.user)
            Recensione.objects.create(prodotto=prodotto,user=user,data_pub=datetime.now())


