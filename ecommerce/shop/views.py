from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')

def profile(request):
    return render(request, 'profile.html')

def payment(request):
    return render(request, 'payment.html')

def demo(request):
    context={
        'name':'Mobile Phone',
        'category': 'Electronics',
        'stock': 100
    }
    context_tags = {
        'num': 10,
    }
    ele_items = {
        'electronics': ['Laptop', 'Mobile', 'Tablet', 'Camera'],
    }
    return render(request, 'var_and_tags.html', {**context, **context_tags, **ele_items})