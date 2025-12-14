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
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

# Menu item page
def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = None
    return render(request, 'menu_item.html', {"menu_item": menu_item})
