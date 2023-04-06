from django.shortcuts import render
from .models import product

from django.http import HttpResponse
from math import ceil

# Create your views here.


def index(request):
    products =product.objects.all()
    n=len(products)
    nSlide=n//4+ceil((n/4)-(n//4))
    element={'product':products,'no. of slides':nSlide,'range':range(1,nSlide)}

    return render(request, 'shop/shop.html',element)


def about(request):
   return render(request,'shop/basic.html')


def contact(request):
    return HttpResponse("we at contactus")


def tracker(request):
    return HttpResponse("we at tracking")


def search(request):
    return HttpResponse("we at search")


def productview(request):
    return HttpResponse("we at productView")


def checkout(request):
    return HttpResponse("we at checkOut")
