from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    PRODUCT_NAME_MAX_LENGTH = 30
    PRODUCT_NAME_MIN_LENGTH = 3

    PRICE_MAX_DIGITS = 4
    PRICE_DECIMAL_PLACES = 2
    PRICE_MIN_VALUE = 0

    title = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        unique=True,
        validators=[
            MinLengthValidator(PRODUCT_NAME_MIN_LENGTH),
        ]
    )
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_DECIMAL_PLACES,
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ]

    )

    def __str__(self):
        return self.title


class Order(models.Model):
    PRODUCTS_RELATED_NAME = 'products'

    date = models.DateField(
        auto_now_add=True,
    )

    products = models.ManyToManyField(
        Product,
        related_name=PRODUCTS_RELATED_NAME
    )

    def __str__(self):
        return str(self.date)
