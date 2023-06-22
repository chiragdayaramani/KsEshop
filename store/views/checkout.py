from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.contrib.auth.hashers import check_password,make_password
from django.views import  View
import razorpay

class CheckOut(View):
    def post(self,request):
        client = razorpay.Client(auth=("rzp_test_jujH7Hxqphw5Cx", "mpoaB4VQU0d9Ep7DDwR39f5l"))

        DATA = {
                "amount": 100,
                "currency": "INR",
                "receipt": "receipt#1",
                # "notes": {
                # "key1": "value3",
                # "key2": "value2"
                #     }
                    }
        client.order.create(data=DATA)
        print(request.POST)
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_id(list(cart.keys()))
        print(address,phone,customer,cart,products)


        for product in products:
            order = Order(customer=Customer(id=customer),product=product,price=product.price,address=address,phone=phone,quantity=cart.get(str(product.id)))
            print(order.placeOrder())

        request.session['cart']={}
        return redirect('cart')