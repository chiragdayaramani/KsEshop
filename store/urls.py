from store.views import home,login,signup
from store.views.login  import logout
from django.urls import path
from store.views import cart
from store.views.checkout import CheckOut
from store.views.orders import OrderView
from .middlewares.auth import  auth_middleware

urlpatterns = [
 path('',home.Index.as_view(),name='homepage'),
path('signup',signup.SignUp.as_view(),name='signup'),
path('login',login.Login.as_view(),name='login'),
path('logout',logout,name='logout'),
path('cart',  auth_middleware(cart.Cart.as_view()),name='cart'),
path('check-out',CheckOut.as_view(),name='checkout'),
path('orders',auth_middleware(OrderView.as_view()),name='orders')
]