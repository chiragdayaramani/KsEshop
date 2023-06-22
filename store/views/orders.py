# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from store.models.product import Product
# from store.models.category import Category
# from store.models.customer import Customer
# from django.contrib.auth.hashers import check_password,make_password
# from django.views import  View
# from store.models import Order

# from store.middlewares.auth import auth_middleware


# class OrderView(View):
#     def get(self,request):
#         customer = request.session.get('customer')
#         orders = Order.get_orders_by_customer(customer)
#         return render(request,'orders.html',{'orders':orders})


from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})