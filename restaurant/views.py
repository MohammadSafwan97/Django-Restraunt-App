from django.shortcuts import render
from .models import Menu, Booking
from .forms import BookingForm
import json   # ✅ REQUIRED

# Home page
def home(request):
    return render(request, 'index.html')

# About page
def about(request):
    return render(request, 'about.html')

# Booking page
def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form = BookingForm()
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

# Menu page
def menu(request):
    items = Menu.objects.filter(is_available=True)
    return render(request, 'pages/menu.html', {'items': items})

# Auth page
def auth(request):
    return render(request, 'pages/auth.html')

# Menu item page
def display_menu_item(request, pk=None):
    menu_item = Menu.objects.get(pk=pk) if pk else None
    return render(request, 'menu_item.html', {"menu_item": menu_item})

# Orders page (Admin / Orders)
def orders(request):
    orders_data = [
        {
            "id": "ORD-1001",
            "createdAt": "2025-01-15T10:30:00",
            "status": "pending",
            "total": 45.50,
            "items": [
                {
                    "id": "1",
                    "quantity": 2,
                    "menuItem": {
                        "name": "Burger",
                        "price": 10.00
                    }
                },
                {
                    "id": "2",
                    "quantity": 1,
                    "menuItem": {
                        "name": "Pizza",
                        "price": 25.50
                    }
                }
            ]
        }
    ]

    context = {
        "orders_json": json.dumps(orders_data)
    }

    return render(request, "order_page.html", context)

def checkout(request):
    # TEMP: replace with session / DB later
    cart = request.session.get("cart", [])
    user = request.session.get("user", None)

    context = {
        "cart_json": json.dumps(cart),
        "user_json": json.dumps(user),
    }

    return render(request, "pages/checkout.html", context)


def order_confirmation(request, order_id):
    # TEMP mock order (replace with DB later)
    order = {
        "id": order_id,
        "createdAt": "2025-01-15T10:30:00",
        "estimatedDelivery": "2025-01-15T11:15:00",
        "paymentMethod": "card",
        "total": 45.50,
        "deliveryAddress": {
            "street": "123 Main St",
            "city": "New York",
            "state": "NY",
            "zipCode": "10001"
        },
        "items": [
            {
                "id": "1",
                "quantity": 2,
                "menuItem": {
                    "name": "Burger",
                    "price": 10.00,
                    "image": "https://via.placeholder.com/80"
                }
            },
            {
                "id": "2",
                "quantity": 1,
                "menuItem": {
                    "name": "Pizza",
                    "price": 25.50,
                    "image": "https://via.placeholder.com/80"
                }
            }
        ]
    }

    context = {
        "order_json": json.dumps(order)
    }

    return render(request, "pages/order_confirmation.html", context)