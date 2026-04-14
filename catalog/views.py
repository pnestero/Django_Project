from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "home.html", context)


def contacts(request):
    return render(request, "contacts.html")



def info(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "info.html", context)
