"""Negozio_animali_Balugani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from shop_online.views import ricerca_per_animale, Barra_di_ricerca, test, pag_prod, TuttiProdottiView, \
    ListaProdottiView2, filtra_prodotti, NegozioPrincipale, search, carrello
from . import views

appname = "shop_online"

urlpatterns = [
    path("prodotti", NegozioPrincipale, name="prodotti"),
    path("prodotti/<slug:slug_animale>", filtra_prodotti, name="prodottianimale"),
    path("prodotti/<slug:slug_categoria>", filtra_prodotti, name="prodotticategoria"),
    path("prodotti/<slug:slug_animale>/<slug:slug_categoria>", filtra_prodotti, name="prodottianimalecategoria"),
    path("search", search, name="search"),
    path("pagina_prodotto/<slug:slug>", pag_prod, name="pag_prodotto"),
    path("carrello", carrello,name="carrello"),




    path("filtra_prodotti",filtra_prodotti,name="filtra"),
    path("prod_animale/<str:animale>", ricerca_per_animale, name="prod_per_animale"),
    path("barra_di_ricerca/<str:animale>", Barra_di_ricerca.as_view(), name="prod_per_animale"),
    path("test", test, name="test"),

]

# erase_db()
# init_db()
