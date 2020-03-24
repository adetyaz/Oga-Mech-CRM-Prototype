from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('products', products, name='products'),
    path('customer/<int:pk>/', customer, name='customer'),
    path('create_order/<int:pk>/', createOrder, name='create_order'),
    path('update_order/<int:pk>/', updateOrder, name='update_order'),
    path('delete_order/<int:pk>/', deleteOrder, name='delete_order'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
]
