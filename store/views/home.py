from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password,make_password
from django.views import  View


class Index(View):
	def post(self,request):
		product= request.POST.get('product')
		remove=request.POST.get('remove')
		cart=request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				if remove:
					if quantity<=1:
						cart.pop(product)
					else:
						cart[product]=quantity-1
				else:
					cart[product]=quantity+1
			else:
				cart[product]=1
		else:
			cart ={}
			cart[product]=1

		request.session['cart']=cart
		print("Cart-->",request.session['cart'])
		print(product)
		return redirect('homepage')
	
	def get(self,request):
		cart=request.session.get('cart')
		customer_name = request.session.get('customer.name')
		if not cart:
			request.session['cart']={}
		products = None
		categories = Category.get_all_categories()
		categoryId = request.GET.get('category')
		if categoryId:
			products = Product.get_all_products_by_category_id(categoryId)
		else:
			products = Product.get_all_products()
		data={}
		data['products']=products
		data['categories']=categories
		data['customer_name'] = customer_name
		
		return render(request, 'index.html',data)

	