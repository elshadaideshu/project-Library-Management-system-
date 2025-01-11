# api/serializers.py

from rest_framework import serializers
from .models import Book, UserProfile, Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # or specify fields: ['id', 'title', 'author', 'isbn', 'published_date', 'available_copies']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'