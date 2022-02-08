from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)
class Product(models.Model):
    name = models.CharField(max_length=210)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    slug = models.SlugField(max_length=48)
    image = models.ImageField(upload_to="product-images", null=True)
    thumbnail = models.ImageField(upload_to="product-thumbnails", null=True, blank=True)
    generic_name = models.CharField(max_length=100, blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url =self.thumbnail.url
        except:
            url = self.image.url
        return url

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('core:remove_from_cart', kwargs={
            'slug': self.slug
        })

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)# allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

# class OrderItem(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     # order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#
#     @property
#     def get_total(self):
#         total =self.product.price * self.quantity
#         return total
#
#     # def get_total_final_price(self):
#     #     if self.product.price:
#     #         return self.get_total
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=True)
#     transaction_id = models.CharField(max_length=200, null=True)
#
#     products = models.ManyToManyField(OrderItem)
#
#     def __str__(self):
#         return str(self.id)
#
#     @property
#     def get_cart_total(self):
#         orderitems = self.products.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
#     # def get_cart_total(self):
#     #     total = 0
#     #     for order_item in self.products.all():
#     #         total += order_item.get_total()
#     #     return total
#
#
#     @property
#     def get_cart_items(self):
#         orderitems = self.products.all()
#         total = sum([item.quantity for item in orderitems])
#         return total
#
#
# class ShippingAdresses(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     name = models.CharField(max_length=200)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     address = models.CharField(max_length=200, null=True)
#     address2 = models.CharField(max_length=200, null=True, blank=True)
#     city = models.CharField(max_length=200, null=True)
#     state = models.CharField(max_length=200, null=True)
#     zipcode = models.CharField(max_length=200, null=True, blank=True)
#     phone = models.CharField(max_length=200, null=True)
#     phone = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return str(address)
