from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from shop_online.models import Recensione


class RecensioneForm(forms.ModelForm):
    testo = forms.Textarea()
    valore = forms.ChoiceField(choices=[(str(e), e) for e in range(1, 6)], required=True)

    class Meta():
        model = Recensione
        fields = ("testo","valore")
