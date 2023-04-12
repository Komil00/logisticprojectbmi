from .models import Cartransport, Necessary_equipment,\
      Rent_of_special_equipment, Passenger_Transportation

from django import forms


class CartransportForm(forms.ModelForm):
    class Meta:
        model = Cartransport
        fields = '__all__'

    
class Necessary_equipmentForm(forms.ModelForm):
    class Meta:
        model = Necessary_equipment
        fields = '__all__'

class Rent_of_special_equipmentForm(forms.ModelForm):
    class Meta:
        model = Rent_of_special_equipment
        fields = '__all__'

class Passenger_TransportationForm(forms.ModelForm):
    class Meta:
        model = Passenger_Transportation
        fields = '__all__'