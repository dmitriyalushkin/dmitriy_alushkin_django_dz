from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product

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
    return render(request, 'main/categories.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'object': product,
        'title': product.category
    }
    return render(request, 'main/product-detail.html', context)