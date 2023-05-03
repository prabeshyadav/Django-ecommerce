
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import ProductViewSet

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet,basename="products")

urlpatterns =[
    path('',views.index,name="shopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="contaceUs"),
    path('tracker/',views.tracker,name="tracking"),
    path('search/',views.search,name="search"),
    path('products/<int:myid>',views.productview,name="productview"),
    path('checkout/',views.checkout,name="checkout"),
    path('productinfo/',views.product_detail),
    
    path('', include(router.urls)),
    
    
]