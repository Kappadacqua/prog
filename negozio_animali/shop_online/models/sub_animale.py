from django.db import models

from .animale import Animale


class Sottocategoria_animale(models.Model):
    nome = models.CharField(max_length=200)
    animale = models.ForeignKey(Animale, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    @staticmethod
    def ottieni_tutte_le_sottocategorie_animali():
        return Sottocategoria_animale.objects.all()



    class Meta:
        verbose_name_plural = "Sottocategorie_Animali"