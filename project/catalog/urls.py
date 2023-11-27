from django.urls import path

from catalog.views import contacts, home, index, categories, product_detail

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('categories/', categories, name='categories-list'),
    path('product/<int:pk>/', product_detail, name='product-detail')
]