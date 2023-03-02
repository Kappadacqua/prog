from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)

    def get_absolute_url(self):
        """lista articoli per specifica categoria"""
        return reverse("dettaglio_categoria:",kwargs={"slug": self.slug})

    @staticmethod
    def ottieni_tutte_le_categorie():
        return Categoria.objects.all()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Categorie"
