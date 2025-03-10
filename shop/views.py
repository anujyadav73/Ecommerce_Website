from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact
from math import ceil

# Create your views here.

def shop_index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params = {'allProds':allProds}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides), 'product': products}
                

    return render(request, 'shop/index.html', params)

#    return HttpResponse("Hello, world. You're at the shop index.")
def shop_about(request):
    return render(request, 'shop/about.html')

def contact(request):

    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def shop_tracker(request):
    return render(request, 'shop/tracker.html')

def shop_search(request):
    return render(request, 'shop/search.html')

def shop_productview(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product':product[0]})

def shop_checkout(request):
    return render(request, 'shop/checkout.html')

def shop_cart(request):
    return render(request, 'shop/cart.html')
