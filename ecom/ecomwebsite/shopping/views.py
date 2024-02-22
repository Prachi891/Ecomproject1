from django.shortcuts import render
from.models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    products_objects =Product.objects.all()
    

#search code

    item_value= request.GET.get('item_value')
    if item_value !='' and item_value is not None:
        products_objects=products_objects.filter(title__icontains=item_value)
      
    paginator = Paginator(products_objects,4)
    page=request.GET.get('page')
    products_objects=paginator.get_page(page)

    return render(request,'index.html',{"products_objects":products_objects})

def detail(request,id):
    products_objects=Product.objects.get(id=id)
    return render(request,'detail.html',{"products_objects":products_objects})

def checkout(request):
    return render(request,'checkout.html')



    
