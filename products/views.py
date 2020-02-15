from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Catagory,Prod
from django.http import HttpResponse

# Create your views here.

def prod(request):
    return render(request,'index.html')

class catagory(ListView):
    model =Catagory
    template_name = 'index.html'

class Product(ListView):
    queryset = Prod.objects.filter(catagory__slug='hex_bolt')
    template_name = 'product.html'

def list_of_catagory(request,catagory_slug):
    catagories=Catagory.objects.all()
    post=Prod.objects.filter(status='publish')
    if catagory_slug:
        catagory=get_object_or_404(Catagory,slug=catagory_slug)
        post=post.filter(catagory=catagory)
    context={'catagories':catagories,'post':post,'catagory':catagory}
    return render(request,'home.html',context)
