from django import template

register = template.Library()

@register.filter()
def range_custom(a):
    return range(a)