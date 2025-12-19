from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Menu, Booking, Order, OrderItem, Address
from .forms import BookingForm
import json


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book")
    else:
        form = BookingForm()

    return render(request, "book.html", {"form": form})


def menu(request):
    items = Menu.objects.filter(is_available=True)
    return render(request, "pages/menu.html", {"items": items})


# ================= AUTH =================

def signin_view(request):
    if request.method != "POST":
        return redirect("home")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "").strip()

    if not username or not password:
        messages.error(request, "Username and password are required")
        return redirect("home")

    user = authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, "Invalid username or password")
        return redirect("home")

    login(request, user)
    return redirect("menu")


def _generate_unique_username(base_username):
    username = base_username
    counter = 1
    while User.objects.filter(username=username).exists():
        username = f"{base_username}_{counter}"
        counter += 1
    return username


def signup_view(request):
    if request.method != "POST":
        return redirect("home")

    base_username = request.POST.get("username", "").strip()
    email = request.POST.get("email", "").strip()
    password = request.POST.get("password", "").strip()

    if not base_username or not email or not password:
        messages.error(request, "All fields are required")
        return redirect("home")

    if User.objects.filter(email=email).exists():
        messages.error(request, "An account with this email already exists")
        return redirect("home")

    username = _generate_unique_username(base_username)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    login(request, user)
    return redirect("menu")


def logout_view(request):
    logout(request)
    return redirect("home")


# ================= MENU ITEM =================

def display_menu_item(request, pk):
    menu_item = Menu.objects.get(pk=pk)
    return render(
        request,
        "menu_item.html",
        {"menu_item": menu_item}
    )


# ================= ORDERS =================

def checkout(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            "Please login or sign up to proceed to checkout"
        )
        return redirect("home")

    return render(request, "pages/checkout.html")


def ordersPage(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            "Please login to view your orders"
        )
        return redirect("home")

    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related("items__menu_item")
        .order_by("-created_at")
    )

    orders_data = [
        {
            "id": order.id,
            "createdAt": order.created_at.isoformat(),
            "status": order.status,
            "total": float(order.total_amount),
            "items": [
                {
                    "id": item.id,
                    "quantity": item.quantity,
                    "menuItem": {
                        "name": item.menu_item.name,
                        "price": float(item.menu_item.price),
                    },
                }
                for item in order.items.all()
            ],
        }
        for order in orders
    ]

    return render(
        request,
        "pages/order_page.html",
        {"orders_json": json.dumps(orders_data)}
    )


def place_order(request):
    if not request.user.is_authenticated:
        messages.error(
            request,
            "Please login or sign up to place an order"
        )
        return redirect("home")

    if request.method != "POST":
        return redirect("menu")

    data = json.loads(request.POST.get("order_data"))

    address = Address.objects.create(
        label="Home",
        street=data["address"]["street"],
        city=data["address"]["city"],
        state=data["address"]["state"],
        zip_code=data["address"]["zipCode"],
    )

    order = Order.objects.create(
        user=request.user,
        payment_method=data["payment"],
        address=address,
        total_amount=data["total"],
    )

    for item in data["cart"]:
        menu_item = Menu.objects.get(id=item["id"])
        OrderItem.objects.create(
            order=order,
            menu_item=menu_item,
            quantity=item["quantity"],
        )

    return redirect("order_confirmation", order_id=order.id)


def order_confirmation(request, order_id):
    if not request.user.is_authenticated:
        messages.error(
            request,
            "Please login to view order confirmation"
        )
        return redirect("home")

    order = Order.objects.get(id=order_id, user=request.user)
    return render(
        request,
        "pages/order_confirmation.html",
        {"order": order}
    )
