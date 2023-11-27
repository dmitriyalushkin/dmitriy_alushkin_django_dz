from django.shortcuts import render

from catalog.models import Category, Product

# Create your views here.


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}):{message}')
    return render(request, 'main/contacts.html')


def home(request):
    return render(request, 'main/home.html')


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
    return render(request, 'main/categories.html', context)


def product_detail(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категории продуктов - {category_item.name}'
    }
    return render(request, 'main/product-detail.html', context)