from .models import Cartransport, Rent_of_special_equipment, Passenger_Transportation
# Create your views here.

from django.shortcuts import render, redirect
from .forms import CartransportForm, Necessary_equipmentForm,\
    Rent_of_special_equipmentForm, Passenger_TransportationForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class CartransportCreateView(CreateView):
    model = Cartransport
    form_class = CartransportForm
    success_url = reverse_lazy('cartransportcreate')
    template_name = 'cartransport.html'

class Rent_of_special_equipmentView(CreateView):
    model = Rent_of_special_equipment
    form_class = Rent_of_special_equipmentForm
    success_url = reverse_lazy('rent_of_special_equipment')
    template_name = 'rent_of_special_equipment.html'

class Passenger_TransportationView(CreateView):
    model = Passenger_Transportation
    form_class = Passenger_TransportationForm
    success_url = reverse_lazy('passenger_transportation')
    template_name = 'passenger_transportation.html'