from django.shortcuts import render, HttpResponse
from .models import Grocerries, Meals
# Create your views here.
def home(request):
    return render(request,'index.html')

def orderMeals(request):
    meals= Meals.objects.all()
    params={"items":meals}
    return render(request,'orderMeals.html',params)

def buyGrocerries(request):
    grocerries=Grocerries.objects.all()
    params={"items":grocerries}
    return render(request,'buyGrocerries.html',params)

def queryFilter(query, item):
    return True

def search(request):
    query=request.Get.get('search')
    Product= Meals.objects.all()
    Product=Grocerries.objects.all()
    print(query)
    productDesc=Product.objects.values(Product,'id')
    print(productDesc)
    prod=[item for item in productDesc if (queryFilter(query, item))]
    print(prod)
    return render(request,'orderMeals.html')

