from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# Create your views here.

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/catalog_home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/catalog_contacts.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/catalog_info.html'
