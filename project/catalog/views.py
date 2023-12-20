from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product, BlogEntry, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}):{message}')
    return render(request, 'main/contacts.html')


@login_required
def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты - Главная'
    }
    return render(request, 'main/index.html', context)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'main/category_list.html'
    extra_context = {
        'title': 'Продукты'
    }


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'main/product-detail.html'


    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['object'] = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = Product.name

        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
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


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.change_product'
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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object

    def test_func(self):
        _user = self.request.user
        _instance: Product = self.get_object()
        custom_perms: tuple = (
            'catalog_app.set_publication',
            'catalog_app.set_category',
            'catalog_app.set_description',
        )

        if _user == _instance.user:
            return True
        elif _user.groups.filter(name='moder') and _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()


class BlogEntryDetailView(LoginRequiredMixin, DetailView):
    model = BlogEntry
    template_name = 'main/blogentry_detail.html'

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.number_of_views += 1
        object.save()
        return object


class BlogEntryListView(LoginRequiredMixin, ListView):
    model = BlogEntry
    template_name = 'main/blogentry_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogEntryCreateView(LoginRequiredMixin, CreateView):
    model = BlogEntry
    fields = ['header', 'content']
    success_url = reverse_lazy('catalog:blog-entry-list')
    template_name = 'main/blogentry_form.html'

    def form_valid(self, form):
        if form.is_valid():
            new_blog_entry = form.save()
            new_blog_entry.slug = slugify(new_blog_entry.header)
            new_blog_entry.save()

        return super().form_valid(form)


class BlogEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogEntry
    fields = ['header', 'content']
    template_name = 'main/blogentry_form.html'
    # success_url = reverse_lazy('main:blog-entry-list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog_entry = form.save()
            new_blog_entry.slug = slugify(new_blog_entry.header)
            new_blog_entry.save()

        return super().form_valid(form)


    def get_success_url(self):

        return reverse('catalog:view', args=[self.kwargs.get('pk')])



