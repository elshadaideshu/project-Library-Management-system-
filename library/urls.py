# api/urls.py

from django.urls import path
from .views import BookListCreateView, BookDetailView
from .views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),  # For listing and creating books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # For retrieving, updating, and deleting a specific book
    

]