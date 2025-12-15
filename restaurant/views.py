from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
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
            form = BookingForm()
    else:
        form = BookingForm()

    return render(request, "book.html", {"form": form})


def menu(request):
    items = Menu.objects.filter(is_available=True)
    return render(request, "pages/menu.html", {"items": items})


def auth(request):
    return render(request, "pages/auth.html")


def display_menu_item(request, pk=None):
    menu_item = Menu.objects.get(pk=pk) if pk else None
    return render(request, "menu_item.html", {"menu_item": menu_item})


def checkout(request):
    return render(request, "pages/checkout.html")


def ordersPage(request):
    orders = (
        Order.objects
        .prefetch_related("items__menu_item")
        .order_by("-created_at")
    )

    orders_data = []
    for order in orders:
        orders_data.append({
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
                    }
                }
                for item in order.items.all()
            ]
        })

    return render(
        request,
        "pages/order_page.html",
        {"orders_json": json.dumps(orders_data)}
    )


@csrf_exempt
def place_order(request):
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

    return redirect(
        "order_confirmation",
        order_id=order.id
    )


def order_confirmation(request, order_id):
    order = (
        Order.objects
        .prefetch_related("items__menu_item")
        .get(id=order_id)
    )

    return render(
        request,
        "pages/order_confirmation.html",
        {"order": order}
    )
