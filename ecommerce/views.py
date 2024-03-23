from django.http import HttpResponse
from django.shortcuts import render,redirect
from app.models import Slider,Banner,Main_Categroy,Product


def base(request):
    return render (request,'base.html')


def home (request):
    sliders = Slider.objects.all()
    
    banners = Banner.objects.all()

    product = Product.objects.filter(Section__name = 'Top Deal Of The Day')
    
    main_categroy = Main_Categroy.objects.all()
    context = {
        'sliders':sliders,
        'banners':banners,
        'main_categroy': main_categroy,
        'product':product,
    }
    return render (request,'home.html',context)


def PRODUCT_DETAILS (request,slug):
    product = Product.objects.get(slug = slug)

    data = {
        'product':product,
    }

    return render (request,'product/product_detail.html',data)


