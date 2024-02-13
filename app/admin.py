from django.contrib import admin
from .models import Slider,Banner,Main_Categroy,Categroy,Sub_Categroy
from .models import Section,Product,Product_Image,Additional_Information
# Register your models here.


class Product_Images(admin.TabularInline):
    model = Product_Image


class Additional_Informations(admin.TabularInline):
    model = Additional_Information


class Product_Admin(admin.ModelAdmin):
    inlines = (Additional_Informations,Product_Images)    
    
    list_display = ('Product_Name','Price','Categroy','Section')
    list_editable = ('Price','Categroy','Section')





admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(Main_Categroy)
admin.site.register(Categroy)
admin.site.register(Sub_Categroy)




admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
