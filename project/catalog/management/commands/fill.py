from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'красная', 'price': 20, 'category': 'ручка'},
            {'name': 'синяя', 'price': 10, 'category': 'ручка'},
            {'name': 'зеленая', 'price': 50, 'category': 'ручка'}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
