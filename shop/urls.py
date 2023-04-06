
from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="shopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="contaceUs"),
    path('tracker/',views.tracker,name="tracking"),
    path('search/',views.search,name="search"),
    path('product/',views.productview,name="productview"),
    path('checkout/',views.checkout,name="checkout"),
    
    
]