import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Negozio_animali_Balugani.settings")

import django

django.setup()

from faker import factory, Faker
from shop_online.models import *
from model_bakery.recipe import Recipe, foreign_key

fake = Faker()

for k in range(100):
    animale = Recipe(Animale,
                     name=fake.name(), )

    categoria = Recipe(Categoria,
                       name=fake.name(), )

    prodotto = Recipe(Prodotto,
                      nome_prodotto=fake.name(),
                      animale=foreign_key(animale),
                      categoria=foreign_key(categoria),
                      venditore=fake.name(),
                      descrizione=fake.sentence(nb_words=6, variable_nb_words=True))
    prodotto.make()

"""
 nome_prodotto = models.CharField(max_length=100)
    animale = models.ForeignKey(Animale, on_delete=models.CASCADE, default=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    venditore = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    prezzo= models.DecimalField(max_digits=12, decimal_places=2, default=0)
    immagine=models.ImageField(null=False, upload_to='static/uploads/',default="3298693.png")
    in_stock= models.BooleanField(default=True)
    slug=models.SlugField(unique=True,max_length=200,default="prova")

    cucciolo = models.BooleanField(default=False)
    adulto = models.BooleanField(default=False)
    anziano = models.BooleanField(default=False)

"""
