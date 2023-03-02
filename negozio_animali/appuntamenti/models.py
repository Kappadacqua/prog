from django.db import models

from negozio_animali.account.models import CustomUser


class Appuntamento(models.Model):

    utente = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    richiesta_appuntamento = models.TextField(blank=True)
    data_richiesta = models.DateField(auto_now_add=True)
    accettazione = models.BooleanField(default=False)
    data_accettata = models.DateField(auto_now_add=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Appuntamenti"