from django.shortcuts import render
from .forms import BookInfoForm
from .models import AddBookInfo


def add_book_info(request):
    forms = BookInfoForm()
    if request.method=='POST':
        forms = BookInfoForm(request.POST)
        if forms.is_valid():
            title = forms.cleaned_data['title']
            author = forms.cleaned_data['author']
            genre = forms.cleaned_data['genre']
            published_date = forms.cleaned_data['publication_date']
            price = forms.cleaned_data['price']
        #normal forms
        #print(title, author, genre, published_date)

        #model forms: add data to table AddBookInfor
        AddBookInfo.objects.create(
            title = title, 
            author = author, 
            genre = genre, 
            published_date = published_date, 
            price = price)

    return render (request, 'add_book_info.html', {'form':forms})        


def render_book_info(request):
    books_info = AddBookInfo.objects.all()
    return render(request, 'render_book_info.html', {'books_info':books_info})