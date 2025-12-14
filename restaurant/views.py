from django.shortcuts import render
from .models import Menu, Booking
from .forms import BookingForm

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
            form = BookingForm()  # Reset form after saving
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

# Menu page
def menu(request):
    items = Menu.objects.filter(is_available=True)
    return render(request, 'pages/menu.html', {'items': items})


# Menu item page
def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = None
    return render(request, 'menu_item.html', {"menu_item": menu_item})
