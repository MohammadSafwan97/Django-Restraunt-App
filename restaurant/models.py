from django.db import models
from django.utils import timezone


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
    price = models.DecimalField(max_digits=6, decimal_places=2)

    image_url = models.URLField(blank=True)  # ✅ TEMP FIX

    category = models.CharField(max_length=20, default="main")
    is_vegetarian = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.name
