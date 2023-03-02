from django.shortcuts import render

from mappa.models import Location


def pagina_informativa(request):
    locations = Location.objects.all()
    if locations:
        ctx = {"location": locations[0]}  # TODO implementare logica per multiple locations
    else:
        ctx = {"location": Location.objects.create(indirizzo="", citta="", stato="")}

    return render(request, template_name="mappa/mappa.html", context=ctx)
