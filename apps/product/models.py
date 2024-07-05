from apps.account.models import User
from apps.catalog.models import Catalog
from apps.core.models import AuditModel, TimeStampedModel
from django.db import models


class ProductCategory(TimeStampedModel, AuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Product(TimeStampedModel, AuditModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_item_count = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    catalog = models.ForeignKey(
        Catalog, on_delete=models.CASCADE, related_name="products"
    )


class ProductReview(TimeStampedModel, AuditModel):
    rating = models.IntegerField()
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
