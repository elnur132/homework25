from django.forms import ModelForm
from .models import IceCream

class IceCreamForm(ModelForm):
    class Meta:
        model = IceCream
        fields = ('name', 'taste')