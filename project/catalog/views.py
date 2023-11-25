from django.shortcuts import render

from catalog.models import Category

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
        'object_list': Category.objects.all()
    }
    return render(request, 'main/base.html', context)