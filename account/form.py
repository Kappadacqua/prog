from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation
from account.models import CustomUser
from django.utils.translation import gettext_lazy as _

convalida_username = UnicodeUsernameValidator()


class RegistrazioneForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label=_('Username'),
        min_length=4,
        max_length=50,
        help_text=_('Username richiesto'),
        validators=[convalida_username],
        error_messages={'unique': _("Username già preso")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
                           max_length=50, help_text='Nome', min_length=4, required=True)
    cognome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cognome'}),
                              max_length=50, help_text='Cognome', min_length=4, required=True)
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
                               max_length=10, help_text='es: 0123456789')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required=True,
                             max_length=100,
                             help_text='Inserisci il tuo indirizzo email')

    password = forms.CharField(label=_('Password'),
                               widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
                               help_text=password_validation.password_validators_help_text_html())
    password_check = forms.CharField(label=_('Conferma password'),
                                     widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                     max_length=100,
                                     help_text=_('Immetti la stessa password per confermare'))

    citta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Citta'}),
                            max_length=50, help_text='Citta', min_length=4, required=True)
    indirizzo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indirizzo'}),
                                max_length=100, help_text='Indirizzo', min_length=4, required=True)
    codice_postale = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codice postale'}),
        help_text='Codice_postale', min_length=5, max_length=5, required=True)

    class Meta():
        model = CustomUser
        fields = (
            "username", "nome", "cognome", "email", "password", "password_check", "telefono", "citta", "indirizzo",
            "codice_postale")


class loginUtenteForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'login-password'}))


class modificaUtenteForm(forms.ModelForm):
    username = forms.CharField(
        required=True,
        label=_('Username'),
        min_length=4,
        max_length=50,
        help_text=_('Username richiesto'),
        validators=[convalida_username],
        error_messages={'unique': _("Username già preso")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
                           max_length=50, help_text='Nome', min_length=4, required=True)
    cognome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cognome'}),
                              max_length=50, help_text='Cognome', min_length=4, required=True)
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
                               max_length=10, help_text='es: 0123456789')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                             required=True,
                             max_length=100,
                             help_text='Inserisci il tuo indirizzo email')
    citta = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Citta'}),
                            max_length=50, help_text='Citta', min_length=4, required=True)
    indirizzo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indirizzo'}),
                                max_length=100, help_text='Indirizzo', min_length=4, required=True)
    codice_postale = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codice postale'}),
        help_text='Codice_postale', min_length=5, max_length=5, required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "nome", "cognome", "email", "telefono", "citta", "indirizzo",
                  "codice_postale")
