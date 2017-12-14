from django import forms
from .models import Excursion, Destination, Customer


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'


class ExcursionForm(forms.ModelForm):
    class Meta:
        model = Excursion
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
