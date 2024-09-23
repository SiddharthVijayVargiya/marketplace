from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marketplace/', views.mango_marketplace, name='marketplace'),
    path('seller/', views.seller_view, name='seller'),
    path('buyer/', views.buyer_view, name='buyer'),
    path('place_order/<int:mango_id>/', views.place_order, name='place_order'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('seller/products/', views.seller_products, name='seller_products'),
    path('delete_mango/<int:mango_id>/', views.delete_mango, name='delete_mango'),
   
    ]
