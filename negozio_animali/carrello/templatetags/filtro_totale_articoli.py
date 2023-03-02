
from django import template

register = template.Library()

@register.filter()
def totale_articoli(dizionario):
    try:
        return sum(dizionario.values())
    except AttributeError:
        return 0
