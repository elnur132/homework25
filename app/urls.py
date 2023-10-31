from django.urls import path
from .views import CreateIceCream, IceList

urlpatterns = [
    path('', IceList.as_view(), name='list'),
    path('icecream/', CreateIceCream.as_view(), name='add_ice')
]
