from django.contrib import admin

from .models import Prodotto, Animale, Categoria, Recensione


@admin.register(Animale)
class AnimaleAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug",]
    prepopulated_fields = {"slug": ( "nome",)}


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["nome", "slug",]
    prepopulated_fields = {"slug": ("nome",)}


@admin.register(Recensione)
class RecensioneAdmin(admin.ModelAdmin):
    list_display = ["prodotto", "testo", "valore"]


@admin.register(Prodotto)
class ProdottoAdmin(admin.ModelAdmin):
    list_display = [
    "nome", "venditore", "in_promo", "descrizione", "prezzo", "immagine", "slug", "in_stock",
    "creato", "cucciolo", "adulto", "anziano"]
    list_filter = ["in_stock"]
    list_editable = ["in_promo", "prezzo", "in_stock"]
    prepopulated_fields = {"slug": ("nome",)}

