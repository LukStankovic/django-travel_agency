from django import forms
from .models import Excursion, Destination, Customer


class AddDestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'
