from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=35)
    category_slug = models.SlugField(blank=True,null=True)

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

class Location(models.Model):
    location = models.CharField(max_length=500)


class Store(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='store')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='store')
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='store')
    store_name = models.CharField(max_length=150)
    description = models.TextField()
    store_slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.store_slug = slugify(self.store_name)
        super(Store, self).save(*args, **kwargs)


class Order(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='order')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
    order_details  = models.TextField()
    active = models.BooleanField(default=True)
    customer_location = models.CharField(max_length=500)
    shipment_location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='order' ,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    pay = models.BooleanField(default=False)

class Offer(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='offer')
    user_delivery_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='offer')
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Bill(models.Model):
    bill_text = models.TextField()
    bill_img = models.ImageField(upload_to='bills/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order = models.IntegerField(blank=True,null=True)

class Bills(models.Model):
    bill_text = models.TextField()
    bill_img = models.ImageField(upload_to='bills/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    order = models.OneToOneField(Order,on_delete=models.CASCADE)


class OrderActive(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_active')
    offer = models.ForeignKey(Offer,on_delete=models.CASCADE,related_name='order_active')
    bill = models.OneToOneField(Bill,on_delete=models.CASCADE,related_name='order_active')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)