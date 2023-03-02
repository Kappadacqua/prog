from datetime import datetime
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from Negozio_animali_Balugani import settings
from shop_online.models import Prodotto


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    costo_totale = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                       validators=[MinValueValidator(Decimal('0.01'))])
    data_creazione = models.DateField(default=datetime.today)
    stato_pagamento = models.BooleanField(default=False)
    chiave_ordine = models.CharField(max_length=250)


class OrderItem(models.Model):
    ordine = models.ForeignKey(Order, related_name='articoli', on_delete=models.CASCADE)
    prodotto = models.ForeignKey(Prodotto,
                                 related_name='articoli_ordinati', on_delete=models.CASCADE)

    prezzo = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                 validators=[MinValueValidator(Decimal('0.01'))])
    quantita = models.IntegerField(default=1)
