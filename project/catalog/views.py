from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product, BlogEntry

from django.views.generic import ListView, DetailView

# Create your views here.


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}):{message}')
    return render(request, 'main/contacts.html')


def index(request):
    context = {
        'object_list': Category.objects.all()[:2],
        'title': 'Продукты - Главная'
    }
    return render(request, 'main/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Продукты'
    }
    return render(request, 'main/category_list.html', context)


def product_detail(request, pk):
    product = Category.objects.get(pk=pk)

    context = {
        'object': Product.objects.filter(category_id=pk),
        'title': product.name
    }
    return render(request, 'main/product-detail.html', context)


# class CategoryListView(ListView):
#     model = Category
#     extra_context = {
#         'title': 'Продукты'
#     }


# class ProductListView(ListView):
#     model = Product
#
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#         context_data['object'] = get_object_or_404(Product, pk=self.kwargs.get('pk'))
#         context_data['title'] = Product.category
#
#         return context_data
#
#
# class BlogEntryDetailView(DetailView):
#     model = BlogEntry
#
#     def get_object(self, queryset=None):
#         self.object = super().get_object(queryset)
#         self.object.views_count += 1
#         self.object.save()
#         return self.object
#
#
# class BlogEntryListView(ListView):
#     model = BlogEntry
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset(*args, **kwargs)
#         queryset = queryset.filter(sign_of_publication=True)
#         return queryset
