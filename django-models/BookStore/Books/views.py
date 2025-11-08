from django.shortcuts import render
from Books.models import Books, BooksTypes

def product_list(request):
    product_list = Books.objects.all()  # Fetch all books from the database
    return render(request, 'product_list.html', {'product_list': product_list})

def book_types(request):
    book_types = BooksTypes.objects.all()  # Fetch all book types from the database
    return render(request, 'book_types.html', {'book_types': book_types})