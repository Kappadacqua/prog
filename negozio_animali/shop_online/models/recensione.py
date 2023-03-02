from datetime import datetime

from django.db import models

from Negozio_animali_Balugani import settings
from shop_online.models import Prodotto


class Recensione(models.Model):
    #utente = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    testo = models.TextField(blank=True)
    valore = models.PositiveIntegerField(choices=[(str(e), e) for e in range(1, 6)])
    data_pub=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.testo

    class Meta:
        verbose_name_plural = "Recensioni"
        ordering = ['-data_pub']