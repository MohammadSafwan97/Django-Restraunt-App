from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),

    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),

    path("auth/", views.auth, name="auth"),

    path("orders/", views.ordersPage, name="ordersPage"),

    path("checkout/", views.checkout, name="checkout"),
    path("place-order/", views.place_order, name="place_order"),

    path(
        "order-confirmation/<int:order_id>/",
        views.order_confirmation,
        name="order_confirmation",
    ),
]
