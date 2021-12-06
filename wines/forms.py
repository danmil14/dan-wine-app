## wines/forms.py
from django import forms
from wines.models import Wine

class WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ('wine_name', 'price', 'varietal', 'description')
