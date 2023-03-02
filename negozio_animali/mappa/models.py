from django.db import models

# Create your models here.
class Location(models.Model):

    citta = models.CharField(max_length=200)
    indirizzo = models.CharField(max_length=200)
    stato = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.indirizzo} {self.citta} {self.stato}"