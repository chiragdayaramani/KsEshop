# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from store.models.product import Product
# from store.models.category import Category
# from store.models.customer import Customer
# from django.contrib.auth.hashers import check_password,make_password
# from django.views import  View


# class Login(View):
# 	return_url = None
# 	def get(self,request):
# 		Login.return_url = request.GET.get('return_url')
# 		return render(request,'login.html')
# 	def post(self,request):
# 		email=request.POST.get('email')
# 		password=request.POST.get('password')
# 		customer=Customer.get_customer_by_email(email)
# 		print(customer.password)
# 		error_message=None
# 		if customer:
# 			print("YEs customer is true.")
# 			flag=check_password(password,customer.password)
# 			if not flag:
# 				error_message='Invalid Email or Password.'	
# 			else:
# 				request.session['customer']=customer.id
# 				return redirect('homepage')
				
# 		else:
# 			print('_________')
# 			print("Customer is wrong.")
# 			error_message='Invalid Email or Password.'
# 		print("___________")
# 		print(customer)
# 		print(email,password,error_message)
# 		return render(request,'login.html',{'error':error_message})
	


# def logout(request):
# 	request.session.clear()
# 	return redirect('login')

from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')

		
	
    

