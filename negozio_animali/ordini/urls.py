from django.urls import path
from ordini.views import crea_ordine, history

appname="ordini"

urlpatterns = [
    path("crea_ordine/", crea_ordine, name="crea_ordine"),
    path("history/", history, name="history")
]
