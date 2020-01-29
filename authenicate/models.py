from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class MyUser(AbstractUser):
    cash = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=10000.00,
        validators=[MinValueValidator(Decimal('0.00'))]
    )


