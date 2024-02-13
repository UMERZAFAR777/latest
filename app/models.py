from django.db import models
from ckeditor.fields import RichTextField



class Slider(models.Model):
    DISCOUNT_DEAL = (
        ('Hot Deals', 'Hot Deals'),
        ('New Arrivals', 'New Arrivals'),
    )

    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL, max_length=200)
    Sales = models.IntegerField()
    Brand_name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_name


class Banner(models.Model):
    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Quote = models.CharField(max_length = 100)


    def __str__(self):
        return self.Quote



class Main_Categroy(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

class Categroy(models.Model):
    main_categroy = models.ForeignKey(Main_Categroy , on_delete = models.CASCADE )
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name +"--"+ self.main_categroy.name


class Sub_Categroy(models.Model):
    categroy  = models.ForeignKey(Categroy,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.categroy.main_categroy.name +"--"+ self.categroy.name +"--"+ self.name



class Section(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    Total_Quantity = models.IntegerField()
    Availbility = models.IntegerField()
    Featured_Image = models.CharField(max_length = 100)
    Product_Name = models.CharField(max_length = 100)
    Price = models.IntegerField()
    Discount = models.IntegerField()
    Product_information = RichTextField()
    Model_Name = models.CharField(max_length = 100)
    Categroy = models.ForeignKey(Categroy,on_delete = models.CASCADE)
    Tags = models.CharField(max_length = 100)
    Description = RichTextField()
    Section = models.ForeignKey(Section,on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.Product_Name


class Product_Image(models.Model):
    Product = models.ForeignKey(Product,on_delete = models.CASCADE)
    Image_url = models.CharField(max_length = 100)


class Additional_Information(models.Model):
    Product = models.ForeignKey(Product,on_delete = models.CASCADE)   
    Specification = models.CharField(max_length = 100)
    detail = models.CharField(max_length = 100)














        

