🍽️ Safwan Restaurant – Django Food Ordering App

A full-stack food ordering web application built with Django, Tailwind CSS, and Vanilla JavaScript.
This project is part of my portfolio and focuses on building a real-world backend-driven application without using frontend frameworks.

🚧 Actively under development and continuously improving

✨ Features

User authentication (signup, login, logout)

Modal-based authentication UI

Browse restaurant menu

Add & remove items from cart

Cart persisted using browser localStorage

Checkout flow with order creation

Order confirmation page

User-specific orders page

Django admin panel for management

Responsive design (mobile & desktop)

Clean relational database models

🛠️ Tech Stack
Backend

Django

SQLite (development)

Django Authentication

Django Admin

Frontend

Django Templates (HTML)

Tailwind CSS

Vanilla JavaScript

State Management

Browser localStorage (cart)

📁 Project Structure
littlelemon/
├── restaurant/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│
├── templates/
│   ├── base.html
│   ├── pages/
│   │   ├── menu.html
│   │   ├── checkout.html
│   │   ├── order_page.html
│   │   └── order_confirmation.html
│   └── partials/
│       ├── header.html
│       ├── cart_sidebar.html
│       └── auth_modal.html
│
├── static/
│   ├── js/
│   │   ├── cart.js
│   │   └── menu.js
│   └── img/
│
├── manage.py

🔄 How the Application Works

User browses the menu

Items are added to cart (stored in localStorage)

Checkout page reads cart data

Order is submitted to Django backend

Backend creates:

Address

Order

Order Items

User is redirected to order confirmation

Orders are visible on:

Orders page

Django Admin panel

🚀 Setup Instructions
git clone https://github.com/MohammadSafwan97/Django-Restraunt-App.git
cd safwan-restaurant

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Open in browser:
👉 http://127.0.0.1:8000/

🔐 Admin Panel

Admin URL:
👉 http://127.0.0.1:8000/admin/

Admin capabilities:

Manage menu items

View and update orders

Manage users

🚧 Project Status

Work in Progress

This project is actively evolving as I:

Refactor code

Improve UX

Add new features

Apply backend best practices

🎯 Roadmap

Password reset & email verification

Convert frontend to React

Expose backend as REST API (DRF)

Real payment gateway integration

Improve mobile UX & animations

Deploy to production

👤 Author

Safwan
Computer Science Student
Portfolio Project – Django & Backend Development