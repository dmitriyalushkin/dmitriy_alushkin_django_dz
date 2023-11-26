from django.urls import path

from catalog.views import contacts, home, index, categories, categories_product

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts),
    path('home/', home),
    path('index/', index),
    path('categories/', categories),
    path('<int:pk>/catalog/', categories_product)
]