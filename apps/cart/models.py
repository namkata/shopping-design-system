from apps.account.models import User
from apps.core.models import AuditModel, TimeStampedModel
from apps.product.models import Product
from django.db import models


class ShoppingCart(TimeStampedModel, AuditModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through="CartItem")


class CartItem(TimeStampedModel, AuditModel):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
