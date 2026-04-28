from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("info/<int:pk>/", ProductDetailView.as_view(), name="catalog_info"),

    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)