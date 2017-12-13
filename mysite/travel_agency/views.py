from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader

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
