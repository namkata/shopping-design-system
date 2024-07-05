from django.contrib import admin

from .models import Product, ProductCategory, ProductReview


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "available_item_count",
        "category",
        "catalog",
    ]
    list_filter = ["category", "catalog"]
    search_fields = ["name"]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "rating"]
    list_filter = ["product", "rating"]
    search_fields = ["product__name", "user__username"]
