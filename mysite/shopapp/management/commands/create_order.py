from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    "Creates orders"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating orders")
        user = User.objects.get(username="admin")
        order, created = Order.objects.get_or_create(
            delivery_address="ul Pupkina, d 8",
            promocode="SALE123",
            user=user,
        )
        self.stdout.write(
            self.style.SUCCESS(f"Created order {order}, from scratch: {created}")
        )
