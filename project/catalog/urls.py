from django.urls import path

from catalog.views import contacts, home, index

urlpatterns = [
    path('contacts/', contacts),
    path('home/', home),
    path('index/', index)
]