# library/urls.py

from django.urls import path
from .views import create_book, checkout_book, CustomAuthToken

urlpatterns = [
    path('books/', create_book, name='create-book'),
    path('books/<int:pk>/checkout/', checkout_book, name='checkout-book'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]