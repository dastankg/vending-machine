from django.contrib import admin
from .models import Product


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "count")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
