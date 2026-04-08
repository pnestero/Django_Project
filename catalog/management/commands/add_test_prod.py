from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Удаление всех продуктов и добавление новых'

    def handle(self, *args, **kwargs):
        # удаление
        Product.objects.all().delete()
        Category.objects.all().delete()

        # создание данных
        cat = Category.objects.create(name='тестовая категория', description='тесты категории')

        products_list = [
            {'name': 'Товар 1', 'price': 100, 'category': cat},
            {'name': 'Товар 2', 'price': 200, 'category': cat},
        ]

        for product in products_list:
            Product.objects.create(**product)

        self.stdout.write(self.style.SUCCESS(f'Внесено в базу {len(products_list)}'))
