from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        category_list = [
            {'name': 'пряник', 'description': 'вкусный'},
            {'name': 'сок', 'description': 'яблочный'}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)



        product_list = [
            {'name': 'тульский', 'price': 50, 'category': 25},
            {'name': 'добрый', 'price': 100, 'category': 26}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)

