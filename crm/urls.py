from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('customer/<int:pk>/', customer, name='customer'),
    path('create_order/', createOrder, name='create_order'),
    path('update_order/<int:pk>/', updateOrder, name='update_order'),
    path('delete_order/<int:pk>/', deleteOrder, name='delete_order'),
]