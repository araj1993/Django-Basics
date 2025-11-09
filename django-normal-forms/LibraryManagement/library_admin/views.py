from django.shortcuts import render
from .forms import BookInfoForm


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
        print(title, author, genre, published_date)
    return render (request, 'add_book_info.html', {'form':forms})        


