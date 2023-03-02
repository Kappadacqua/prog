from django.contrib import admin
from django.urls import path

from pagamento.views import conferma_ordine,pagamento_effettuato

appname="pagamento"

urlpatterns = [
    path("conferma_ordine/", conferma_ordine, name="conferma_ordine"),
    path("pagamento_effettuato/", pagamento_effettuato, name="pagamento_effettuato"),

]