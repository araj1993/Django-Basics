from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cart/', views.cart, name = 'cart'),
    path('profile/', views.profile, name = 'profile'),
    path('payment/', views.payment, name = 'payment'),
    #template inheritance demo
    path('demo/', views.demo, name = 'demo'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
]
