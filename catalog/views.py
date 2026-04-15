from django.shortcuts import render, get_object_or_404

import catalog
from catalog.models import Product


# Create your views here.
def home(request):
    product = Product.objects.all()
    context = {"products": product}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")



def info(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    context = {"product": product_item}
    return render(request, "info.html", context)

