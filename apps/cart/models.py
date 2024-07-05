from django.db import models

from apps.account.models import User
from apps.core.models import TimeStampedModel, AuditModel
from apps.product.models import Product


class ShoppingCart(TimeStampedModel, AuditModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='CartItem')


class CartItem(TimeStampedModel, AuditModel):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
