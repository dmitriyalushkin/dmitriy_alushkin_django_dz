from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product, BlogEntry, Version

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from django.urls import reverse_lazy, reverse

from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm


# Create your views here.


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'{name} ({phone}):{message}')
#     return render(request, 'main/contacts.html')
#
#
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты - Главная'
    }
    return render(request, 'main/index.html', context)
#
#
# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Продукты'
#     }
#     return render(request, 'main/category_list.html', context)
#
#
# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#
#     context = {
#         'object': product,
#         'title': product.name
#     }
#     return render(request, 'main/product-detail.html', context)

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'object': product,
#         'title': product.category
#     }
#     return render(request, 'main/product-detail.html', context)


class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'
    extra_context = {
        'title': 'Продукты'
    }


class ProductListView(ListView):
    model = Product


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['object'] = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = Product.name

        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    template_name = 'main/product_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    template_name = 'main/product_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


# class BlogEntryDetailView(DetailView):
#     model = BlogEntry
#     template_name = 'main/blogentry_detail.html'
#
#     def get_object(self, queryset=None):
#         object = super().get_object(queryset)
#         object.number_of_views += 1
#         object.save()
#         return object
#
#
# class BlogEntryListView(ListView):
#     model = BlogEntry
#     template_name = 'main/blogentry_list.html'
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset(*args, **kwargs)
#         queryset = queryset.filter(sign_of_publication=True)
#         return queryset
#
#
# class BlogEntryCreateView(CreateView):
#     model = BlogEntry
#     fields = ['header', 'content']
#     success_url = reverse_lazy('catalog:blog-entry-list')
#     template_name = 'main/blogentry_form.html'
#
#     def form_valid(self, form):
#         if form.is_valid():
#             new_blog_entry = form.save()
#             new_blog_entry.slug = slugify(new_blog_entry.header)
#             new_blog_entry.save()
#
#         return super().form_valid(form)
#
#
# class BlogEntryUpdateView(UpdateView):
#     model = BlogEntry
#     fields = ['header', 'content']
#     template_name = 'main/blogentry_form.html'
#     # success_url = reverse_lazy('main:blog-entry-list')
#
#     def form_valid(self, form):
#         if form.is_valid():
#             new_blog_entry = form.save()
#             new_blog_entry.slug = slugify(new_blog_entry.header)
#             new_blog_entry.save()
#
#         return super().form_valid(form)
#
#
#     def get_success_url(self):
#
#         return reverse('catalog:view', args=[self.kwargs.get('pk')])



