from django.shortcuts import render
from .models import product

from django.http import HttpResponse
from math import ceil

# Create your views here.


def index(request):
# products =product.objects.all()
    #n=products.count()
    #n=len(products)
    #nSlide=n//4+ceil((n/4)-(n//4))
    #allproduct=[[products,range(1,nSlide),nSlide],
    #          [products,range(1,nSlide),nSlide]]
    #element={'allproducts':allproduct}
    
    # products= product.objects.all()
    # n= len(products)
    #nSlides= n//4 + ceil((n/4)-(n//4))
    #allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    allprods=[]
    cataprods=product.objects.values('category','id')
    cats ={item['category'] for item in cataprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    element={'allProds': allprods }
# return render(request,"shop/index.html", )

    return render(request, 'shop/shop.html',element)


def about(request):
    return render(request,'shop/about.html')


def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return HttpResponse("we at search")


def productview(request,myid):
    product=product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/producview')


def checkout(request):
    return HttpResponse("we at checkOut")
