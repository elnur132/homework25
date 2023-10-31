from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import IceCream
from .forms import IceCreamForm

# Create your views here.
class CreateIceCream(CreateView):
    model = IceCream
    form_class = IceCreamForm
    template_name = 'form.html'
    success_url = reverse_lazy('list')
    
class IceList(ListView):
    model = IceCream
    template_name = 'list.html'
    context_object_name = 'icecreams'