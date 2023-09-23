from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        order = Order.objects.first()
        if not order:
            self.stdout.write(self.style.ERROR("Order not found. Quit updating."))
            return

        products = Product.objects.all()
        self.stdout.write(f"Products to add: {products}")

        for product in products:
            self.stdout.write(f"Adding product to first order: {product}")
            order.products.add(product)

        order.save()
        self.stdout.write(self.style.SUCCESS("Order updated. All products added."))
