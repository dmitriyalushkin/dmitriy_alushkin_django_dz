from django.urls import path

from catalog.views import contacts, index, categories, product_detail

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories-list'),
    path('product/<int:pk>/', product_detail, name='product-detail')
]