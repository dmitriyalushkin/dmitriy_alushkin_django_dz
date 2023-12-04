from django.urls import path

from catalog.views import contacts, index, product_detail, categories
from catalog.views import index

from catalog.views import CategoryListView, ProductListView
from catalog.views import BlogEntryDetailView, BlogEntryListView, BlogEntryCreateView, BlogEntryUpdateView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category_list/', categories, name='categories-list'),
    path('product/<int:pk>/', product_detail, name='product-detail'),
    path('category_list/', CategoryListView.as_view(), name='categories-list'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product-detail'),
    path('view/<int:pk>/', BlogEntryDetailView.as_view(), name='blog-entry-detail'),
    path('list/', BlogEntryListView.as_view(), name='blog-entry-list'),
    path('create/', BlogEntryCreateView.as_view(), name='blog-entry-create'),
    path('edit/<int:pk>/', BlogEntryUpdateView.as_view(), name='blog-entry-edit')
]