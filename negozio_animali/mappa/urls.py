
from django.urls import path

from mappa.views import pagina_informativa

urlpatterns = [

    path("pagina_informativa/", pagina_informativa, name="pagina_informativa"),
]