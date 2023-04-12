from .models import Cartransport, Necessary_equipment, Rent_of_special_equipment, Passenger_Transportation
# Create your views here.

from django.shortcuts import render, redirect
from .forms import CartransportForm, Necessary_equipmentForm,\
    Rent_of_special_equipmentForm, Passenger_TransportationForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class CartransportCreateView(CreateView):
    model = Cartransport
    form_class = CartransportForm
    # success_url = reverse_lazy('person_list')
    template_name = 'index.htm'