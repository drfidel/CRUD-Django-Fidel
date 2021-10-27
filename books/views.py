from django.shortcuts import render, get_object_or_404
from rest_framework.exceptions import ParseError

# Create your views here.
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser


from .models import BookAuthor, Book
from .bookSerializers import BookSerializer, BookAuthorSerializer

class BookAuthorView(ListCreateAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class SingleBookAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
        

class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
