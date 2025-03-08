from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.shop_index,name='ShopHome'),
    path('about/',views.shop_about,name='ShopAbout'),
    path('contact/',views.shop_contact,name='ShopContact'),
    path('tracker/',views.shop_tracker,name='ShopTracker'),
    path('search/',views.shop_search,name='ShopSearch'),
    path('productview/',views.shop_productview,name='ShopProductView'),
    path('checkout/',views.shop_checkout,name='ShopCheckout'),
    path('cart/',views.shop_cart,name='ShopCart'),
]