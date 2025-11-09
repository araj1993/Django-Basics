from django import forms

class BookInfoForm(forms.Form):
    title = forms.CharField(max_length=100, label='Book Title')
    author = forms.CharField(max_length=100, label='Author Name')
    genre = forms.CharField(max_length=13, label='Genre')
    publication_date = forms.DateField(label='Publication Date', widget=forms.SelectDateWidget)
    price = forms.DecimalField(label='Price')