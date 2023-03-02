from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from .animale import Animale
from .categoria import Categoria
from django.urls import reverse




class Prodotto(models.Model):

    nome = models.CharField(max_length=100)
    animale = models.ForeignKey(Animale, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    venditore = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    prezzo = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(Decimal('0.01'))])
    immagine = models.ImageField(null=False, upload_to='static/uploads/', default="static/prodotti/3298693.png")
    in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=False, unique=True)
    in_promo=models.BooleanField(default=False)

    cucciolo = models.BooleanField(default=True)
    adulto = models.BooleanField(default=True)
    anziano = models.BooleanField(default=True)

    creato = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse("dettaglio_articolo:",kwargs={"slug": self.slug})

    def disponibile(self):
        if self.in_stock:
            return "è attualmente disponibile"
        else:
            return "NON è attualmente disponibile"

    def __str__(self):
        return "ID: " + str(self.pk) + ": " + self.nome + " " + str(self.categoria) + " per " + str(self.animale) + " " + self.venditore + " " + str(
            self.prezzo) + " euro " + self.disponibile()

    @staticmethod
    def tutti_animali():
        return Animale.ottieni_tutti_gli_animali()

    @staticmethod
    def tutte_categorie():
        return Categoria.ottieni_tutte_le_categorie()

    @staticmethod
    def get_prodotto_con_id(id):
        return Prodotto.objects.filter(id__in=id)

    @staticmethod
    def ottieni_tutti_i_prodotti():
        return Prodotto.objects.all()

    @staticmethod
    def get_tutti_i_prodotti_con_animale_id(animale_id):
        if animale_id:
            return Prodotto.objects.filter(animale=animale_id)
        else:
            return Prodotto.ottieni_tutti_i_prodotti()

    @staticmethod
    def get_tutti_i_prodotti_con_categoria_id(categoria_id):
        if categoria_id:
            return Prodotto.objects.filter(categoria=categoria_id)
        else:
            return Prodotto.ottieni_tutti_i_prodotti()


    @staticmethod
    def get_animale_e_categorie_prodotti():
        lista=[[animale,[categoria for categoria in Categoria.ottieni_tutte_le_categorie()]] for animale in Animale.ottieni_tutti_gli_animali()]
        return lista


    def tags(self):
        lista_tags=[]
        if self.cucciolo and self.adulto and self.anziano:
            lista_tags.append("generico")
        if self.cucciolo:
            lista_tags.append("cucciolo")
        if self.adulto:
            lista_tags.append("adulto")
        if self.anziano:
            lista_tags.append("anziano")


        return lista_tags


    class Meta:
        verbose_name_plural = "Prodotti"

    def stampa_bene(self):
        return f"-{self.nome} di {self.venditore}."