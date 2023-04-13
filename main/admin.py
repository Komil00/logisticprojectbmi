from django.contrib import admin
from .models import Cartransport, Rent_of_special_equipment, Passenger_Transportation

# Register your models here.

admin.site.register(Cartransport)
admin.site.register(Rent_of_special_equipment)
admin.site.register(Passenger_Transportation)