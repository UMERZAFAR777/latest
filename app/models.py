from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save



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
    Product_information = RichTextField(null=True)
    Model_Name = models.CharField(max_length = 100)
    Categroy = models.ForeignKey(Categroy,on_delete = models.CASCADE)
    Tags = models.CharField(max_length = 100)
    Description = RichTextField()
    Section = models.ForeignKey(Section,on_delete = models.DO_NOTHING)
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Product_Name


    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.Product_Name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)







class Product_Image(models.Model):
    Product = models.ForeignKey(Product,on_delete = models.CASCADE)
    Image_url = models.CharField(max_length = 100)


class Additional_Information(models.Model):
    Product = models.ForeignKey(Product,on_delete = models.CASCADE)   
    Specification = models.CharField(max_length = 100)
    detail = models.CharField(max_length = 100)














        

