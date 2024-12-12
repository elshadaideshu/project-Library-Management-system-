# library/urls.py

from django.urls import path
from .views import create_book, checkout_book

urlpatterns = [
    path('books/', create_book, name='create-book'),
    path('books/<int:pk>/checkout/', checkout_book, name='checkout-book'),
]