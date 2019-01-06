from django.shortcuts import render
from django.views.generic import DetailView, ListView
from shop.models import *
# Create your views here.

class ProductList(ListView):
    template_name = "items_list.html"
    queryset = Item.objects.all()
    context_object_name = 'items'


class SingleProduct(DetailView):
    model = Item
    template_name = "item_details.html"
    context_object_name = 'item'

