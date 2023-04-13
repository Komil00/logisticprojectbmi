from django.urls import path
from .views import CartransportCreateView, Rent_of_special_equipmentView, Passenger_TransportationView
from django.views.generic import TemplateView,ListView

urlpatterns = [
    path('cartransportcreate', CartransportCreateView.as_view(), name='cartransportcreate'),
    path('rent_of_special_equipment', Rent_of_special_equipmentView.as_view(), name='rent_of_special_equipment'),
    path('passenger_transportation', Passenger_TransportationView.as_view(), name='passenger_transportation'),
    path('about/index.htm/', TemplateView.as_view(template_name='about/index.htm')),
    path('tariffs/index.htm/', TemplateView.as_view(template_name='tariffs/index.htm')),
    path('partners/index.htm/', TemplateView.as_view(template_name='partners/index.htm')),
    path('contacts/index.htm', TemplateView.as_view(template_name='contacts/index.htm')),
]

