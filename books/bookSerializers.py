from rest_framework import serializers

from .models import Book, BookAuthor

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'bookTitle', 'description', 'book_poster' , 'published_date', 'author')

    bookTitle = serializers.CharField(max_length=120)
    description = serializers.CharField()
    book_poster = serializers.ImageField()
    published_date = serializers.DateTimeField()
    

    

class BookAuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = BookAuthor
        fields = ("id","name", "email", "books")

    name = serializers.CharField(max_length=120)
    email = serializers.CharField()

    