from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.form import RegistrazioneForm, modificaUtenteForm


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "account/creazione_utente.html"
    success_url = reverse_lazy("login")



def registrazione(request):
    if request.method == "POST":
        form = RegistrazioneForm(request.POST)
        if form.is_valid():
            print("valido")

            user = form.save(commit=False)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user.username = username
            user.set_password(password)
            user.nome = form.cleaned_data.get("nome")
            user.cognome = form.cleaned_data.get("cognome")
            user.email = form.cleaned_data.get("email")
            user.telefono = form.cleaned_data.get("telefono")
            user.citta = form.cleaned_data.get("citta")
            user.indirizzo = form.cleaned_data.get("indirizzo")
            user.codice_postale = form.cleaned_data.get("codice_postale")
            user.save()

            login(request, user)

            return redirect("/")
    else:
        print("errore")
        form = RegistrazioneForm()
    return render(request, "account/creazione_utente_crispy.html", {"form": form})


@login_required
def user_edit(request):
    if request.method == "POST":
        user_form = modificaUtenteForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = modificaUtenteForm(instance=request.user)

    return render(request, "account/user_edit.html", {"form": user_form})

def profilo(request):
    return render(request, "account/profilo.html")
