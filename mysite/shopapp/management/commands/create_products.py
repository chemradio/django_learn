from django.core.management import BaseCommand

# from mysite.shopapp.models import Product
from shopapp.models import Product


class Command(BaseCommand):
    """Creates products"""

    def handle(self, *args, **kwargs):
        # all_products = Product.objects.all()
        # for prod in all_products:
        #     prod.delete()

        product_names = [
            ("Laptop", 1999, 0),
            ("Desktop", 2999, 10),
            ("Smartphone", 999, 25),
        ]
        for product_name, price, discount in product_names:
            product, created = Product.objects.get_or_create(
                name=product_name, price=price, discount=discount
            )
            self.stdout.write(f"Product: {product.name}, from scratch: {created}")
        self.stdout.write(self.style.SUCCESS("Products created"))
