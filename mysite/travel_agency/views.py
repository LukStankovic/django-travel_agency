from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import DestinationForm, ExcursionForm, CustomerForm

from .models import Excursion, Destination, Customer


def index(request):
    return render_to_response('travel_agency/index.html')


def excursions(request):
    template = loader.get_template('travel_agency/excursions.html')
    all_excursions = Excursion.objects.all()
    context = {'all_excursions': all_excursions}
    return HttpResponse(template.render(context, request))


def excursion_detail(request, id):
    template = loader.get_template('travel_agency/excursion_detail.html')
    excursion = get_object_or_404(Excursion, pk=id)
    context = {'excursion': excursion}
    return HttpResponse(template.render(context, request))


def destinations(request):
    template = loader.get_template('travel_agency/destinations.html')
    all_destinations = Destination.objects.all()
    context = {'all_destinations': all_destinations}
    return HttpResponse(template.render(context, request))


def destination_detail(request, id):
    template = loader.get_template('travel_agency/destination_detail.html')
    destination = get_object_or_404(Destination, pk=id)
    context = {'destination': destination}
    return HttpResponse(template.render(context, request))


def customers(request):
    template = loader.get_template('travel_agency/customers.html')
    all_customers = Customer.objects.all()
    context = {'all_customers': all_customers}
    return HttpResponse(template.render(context, request))


def customer_detail(request, id):
    template = loader.get_template('travel_agency/customer_detail.html')
    customer = get_object_or_404(Customer, pk=id)
    context = {'customer': customer}
    return HttpResponse(template.render(context, request))


# Destination form
def add_destination(request):
    success = False
    template = loader.get_template('travel_agency/add_destination.html')
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            context = {'form': form, 'success': success}
            return HttpResponse(template.render(context, request))
    else:
        form = DestinationForm()
        context = {'form': form, 'success': success}
        return HttpResponse(template.render(context, request))


# Excursion form
def add_excursion(request):
    success = False
    template = loader.get_template('travel_agency/add_excursion.html')
    if request.method == 'POST':
        form = ExcursionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            context = {'form': form, 'success': success}
            return HttpResponse(template.render(context, request))
    else:
        form = ExcursionForm()
        context = {'form': form, 'success': success}
        return HttpResponse(template.render(context, request))


# Registration form
def registration(request):
    success = False
    template = loader.get_template('travel_agency/registration.html')
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            context = {'form': form, 'success': success}
            return HttpResponse(template.render(context, request))
    else:
        form = CustomerForm()
        context = {'form': form, 'success': success}
        return HttpResponse(template.render(context, request))
