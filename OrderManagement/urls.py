from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/', CustomerList),
    path('add/customers/', CustomerAdd),
    path('update/customer/<int:id>/', CustomerUpdate, name='customer_update'),
    path('delete/customer/<int:id>/', CustomerDelete, name='customer_delete'),
    
    path('add/orders/',OrdersAdd),
    path('orders/',OrdersList),
    path('delete/order/<int:id>',OrdersDelete, name='order_delete'),
    path('update/order/<int:id>',OrdersUpdate, name='order_update'),
]