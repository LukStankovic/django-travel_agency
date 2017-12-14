from django import forms
from .models import Excursion, Destination, Customer


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
