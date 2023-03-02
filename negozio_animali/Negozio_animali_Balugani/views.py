from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mappa.models import Location
from shop_online.models import Animale


def base(request):
    return render(request, template_name="base.html")


def home(request):
    ctx = {"lista_animali": Animale.objects.all()}

    return render(request, template_name="home.html", context=ctx)

