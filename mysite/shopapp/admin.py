from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .admin_mixins import ExportAsCSVMixin
from .models import Order, Product


class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description="Archive products")
def mark_archived(
    modeladmin: admin.ModelAdmin,
    request: HttpRequest,
    queryset: QuerySet,
):
    queryset.update(archived=True)


@admin.action(description="Unarchive products")
def mark_unarchived(
    modeladmin: admin.ModelAdmin,
    request: HttpRequest,
    queryset: QuerySet,
):
    queryset.update(archived=False)


# admin.site.register(Product, ProductAdmin)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [mark_archived, mark_unarchived, "export_csv"]
    inlines = [OrderInline]
    list_display = "pk", "name", "description_short", "price", "discount", "archived"
    list_display_links = "pk", "name"
    ordering = ["-pk"]
    search_fields = "name", "description"
    fieldsets = [
        (
            None,
            {
                "fields": ("name", "description"),
            },
        ),
        (
            "Price Options",
            {"fields": ("price",), "classes": ("collapse",)},
        ),
        (
            "Extra Options",
            {
                "fields": ("archived",),
                "classes": ("collapse",),
                "description": "Extra options. Archived - is for soft delete.",
            },
        ),
    ]

    def description_short(self, object: Product) -> str:
        return object.description[:40] + "..."


class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = "pk", "delivery_address", "promocode", "created_at", "user_verbose"

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self, object: Order) -> str:
        return object.user.first_name or object.user.username
