from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True)
    category = models.CharField(max_length=20, default="main")
    is_vegetarian = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    label = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.label} - {self.city}"


class Order(models.Model):
    PAYMENT_CHOICES = [
        ("cash", "Cash"),
        ("card", "Card"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.menu_item.name} × {self.quantity}"
