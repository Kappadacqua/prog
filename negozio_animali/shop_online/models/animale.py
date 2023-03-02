from django.db import models
from django.urls import reverse


class Animale(models.Model):
    """Possibilità di creare molte tipologie di animale"""

    nome = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    def get_absolute_url(self):
        """lista articoli per specifico animale"""
        return reverse("dettaglio_animale:",kwargs={"slug": self.slug})

    @staticmethod
    def ottieni_tutti_gli_animali():
        return Animale.objects.all()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Animali"

