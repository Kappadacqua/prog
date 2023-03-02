from django.contrib import admin
from django.urls import path


from carrello.views import aggiungi_carrello, rimuovi_carrello, visualizza_carrello, paga_carrello

appname="carrello"

urlpatterns = [
    path("aggiungi_carrello/", aggiungi_carrello, name="aggiungi_carrello"),
    path("rimuovi_carrello/", rimuovi_carrello, name="rimuovi_carrello"),
    path("visualizza_carrello/", visualizza_carrello, name="visualizza_carrello"),
    path("paga_carrello/", paga_carrello, name="paga_carrello"),
]