from django.db import models
from django.urls import reverse

# Create your models here.
from authenicate.models import MyUser


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    storage = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'id': self.id})


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    total_cost = models.DecimalField(decimal_places=2, max_digits=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    return_goods = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.buyer.username} BUY {self.product.title} ({self.quantity}) IN {self.created_at}"


class Return(models.Model):
    purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
