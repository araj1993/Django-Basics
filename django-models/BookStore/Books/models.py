from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class BooksTypes(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)