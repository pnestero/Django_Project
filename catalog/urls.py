from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("info/<int:pk>/", ProductDetailView.as_view(), name="catalog_info"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
