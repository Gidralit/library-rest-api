from rest_framework import serializers

from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'year', 'genre', 'category', 'publishing_house', 'image', 'content']

