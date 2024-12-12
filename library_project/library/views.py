# library/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, User
from .serializers import BookSerializer, UserSerializer

@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        book = serializer.save()
        return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def checkout_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        if book.available:
            book.available = False
            book.save()
            return Response({'status': 'book checked out'}, status=status.HTTP_200_OK)
        return Response({'status': 'book not available'}, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)