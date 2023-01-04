from rest_framework import serializers
from .models import Author, Book

class BookSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class AuthorSeriliazer(serializers.ModelSerializer):
    books = BookSeriliazer(read_only=True, many=True)

    class Meta:
        model=Author
        fields="__all__"