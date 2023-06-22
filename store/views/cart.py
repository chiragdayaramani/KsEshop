from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password,make_password
from django.views import  View


class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request,'cart.html',{'products':products})