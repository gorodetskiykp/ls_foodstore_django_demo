from django.shortcuts import render
from .models import Cart, Item


def get_items_list(request):
    template = 'store/items_list.html'
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, template, context)


def get_cart(request):
    template = 'store/cart.html'
    positions = Cart.objects.all()
    context = {
        'positions': positions,
    }
    return render(request, template, context)
