from django.urls import path

from catalog.views import index


from catalog.views import CategoryListView, ProductListView, ProductCreateView, ProductUpdateView
# from catalog.views import BlogEntryDetailView, BlogEntryListView, BlogEntryCreateView, BlogEntryUpdateView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('category_list/', CategoryListView.as_view(), name='category-list'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    # path('view/<int:pk>/', BlogEntryDetailView.as_view(), name='blog-entry-detail'),
    # path('', BlogEntryListView.as_view(), name='blog-entry-list'),
    # path('create/', BlogEntryCreateView.as_view(), name='blog-entry-create'),
    # path('edit/<int:pk>/', BlogEntryUpdateView.as_view(), name='blog-entry-edit')
]