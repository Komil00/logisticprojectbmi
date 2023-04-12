from django.urls import path
from .views import CartransportCreateView

urlpatterns = [
    path('cartransportcreate', CartransportCreateView.as_view(), name='cartransportcreate'),

]

