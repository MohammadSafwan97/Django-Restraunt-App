Safwan Restaurant – Django Food Ordering App

This is a full-stack food ordering web application built using Django, Tailwind CSS, and Vanilla JavaScript.
The project is developed as a portfolio project to practice backend development, frontend integration, and real-world application flow without frontend frameworks.

FEATURES

Browse restaurant menu

Add and remove items from cart

Cart stored in browser using localStorage

Checkout flow with order creation

Order confirmation page

Orders management page

Django admin panel

Responsive layout (mobile and desktop)

Clean backend with real database models

TECH STACK

Backend:

Django

SQLite (default database)

Django Admin

Frontend:

HTML (Django Templates)

Tailwind CSS

Vanilla JavaScript

State Management:

Browser localStorage (cart)

PROJECT STRUCTURE

littlelemon/

restaurant/

models.py

views.py

urls.py

admin.py

forms.py

templates/

base.html

pages/

menu.html

checkout.html

order_page.html

order_confirmation.html

partials/

header.html

cart_sidebar.html

static/

js/

cart.js

menu.js

img/

manage.py

HOW THE APPLICATION WORKS

User browses menu

Items are added to cart (stored in localStorage)

Checkout page reads cart from localStorage

Order is submitted to Django backend

Backend creates:

Address

Order

Order Items

User is redirected to order confirmation page

Orders are visible on the Orders page and Admin panel

SETUP INSTRUCTIONS

Clone the repository:
git clone <repository-url>
cd safwan-restaurant

Create virtual environment:
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac/Linux)

Install Django:
pip install django

Run migrations:
python manage.py migrate

Create admin user:
python manage.py createsuperuser

Run the server:
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

ADMIN PANEL

Admin URL:
http://127.0.0.1:8000/admin/

Admin features:

Manage menu items

View orders

Update order status

PROJECT GOALS & ROADMAP

Current goals:

Understand Django backend architecture

Practice frontend–backend integration

Build a complete ordering flow without frameworks

Learn cart and state management using Vanilla JavaScript

Future goals:

Convert frontend to React

Expose Django backend as REST API

Implement user authentication

Link orders to logged-in users

Add real payment gateway integration

Improve mobile UX and animations

Implement real-time order tracking

Deploy to production environment

NOTES

No frontend frameworks were used intentionally

Cart logic is handled manually in JavaScript

Project focuses on fundamentals and learning

Built for portfolio and educational purposes

AUTHOR

Safwan
Computer Science Student
Portfolio Project