from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, View, CreateView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from . import forms
from .models import Product

from . import models
from django.shortcuts import redirect
from django.http import JsonResponse
import json

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class AboutView(TemplateView):
    template_name = 'about.html'


class StoreProductListView(ListView):
    model = models.Product
    template_name = "store.html"
    paginate_by = 8

class ProductCreateView(CreateView):
    model= Product
    template_name = "product-add.html"
    form_class = forms.ProductCreateForm
    # fields = ('name', 'generic_name', 'price', 'decription', 'image')
    raise_exception = True


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/products/single.html', {'product': product})

class ProductDetailView(DetailView):
    model = models.Product
    template_name = "product.html"

# def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#     context = {'items': items, 'order': order}
#     return render(request, 'cart.html', context)
#
#
# class CartView(View):
#
#     def get(self, *args, **kwargs):
#         try:
#             order = models.Order.objects.get(customer= self.request.user.customer, complete=False)
#             context = {
#                 'object': order
#             }
#             return render(self.request, 'cart.html', context)
#         except ObjectDoesNotExist:
#             messages.warning(self.request, "You do not have an active order")
#             return redirect("/")
#
#
#
# def checkout(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total': 0, 'get_cart_items': 0}
#     context = {'items': items, 'order': order}
#     return render(request, 'checkout.html', context)
#
# class CheckoutView(View):
#
#     def get(self, *args, **kwargs):
#         form = forms.CheckoutFormView()
#         context = {'form': form}
#         return render(self.request, 'checkout.html', context)
#
#     def post(self, *args, **kwargs):
#         form = forms.CheckoutFormView(self.request.POST or None)
#         if form.is_valid():
#             print(form.cleaned_data)
#             print("form is valid")
#             return redirect('core:checkout')
#
# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     print('Action:', action)
#     print('Product:', productId)
#
#     customer = request.user.customer
#     product = models.Product.objects.get(id=productId)
#     order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
#
#     orderItem, created = models.OrderItem.get_or_create('order=order', product=product)
#
#     if action == 'add':
#         orderItem.quantity = (orderItem.quantity + 1)
#     elif action == 'remove':
#         orderItem.quantity = (orderItem.quantity -1)
#
#     orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#
#     return JsonResponse('Item was addded', safe=False)
#
# def add_to_cart(request, slug):
#     product = get_object_or_404(models.Product, slug=slug)
#     order_item, created = models.OrderItem.objects.get_or_create(product=product, customer = request.user.customer)
#     order_qs = models.Order.objects.filter(customer=request.user.customer, complete=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.products.filter(product__slug=product.slug).exists():
#             order_item.quantity += 1
#             messages.info(request, "This item quantity was updated.")
#             order_item.save()
#             return redirect("core:cart")
#         else:
#             order.products.add(order_item)
#             messages.info(request, "This item was added to your cart.")
#             return redirect("core:cart")
#     else:
#         order = models.Order.objects.create(customer=request.user.customer)
#         order.products.add(order_item)
#         messages.info(request, "This item was added to your cart.")
#     return redirect("core:cart")
#
# def remove_from_cart(request, slug):
#     product = get_object_or_404(models.Product, slug=slug)
#     order_qs = models.Order.objects.filter(
#         customer=request.user.customer,
#         complete=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.products.filter(product__slug=product.slug).exists():
#             order_item = models.OrderItem.objects.filter(
#                 product=product,
#                 customer=request.user.customer
#             )[0]
#             order.products.remove(order_item)
#             order_item.delete()
#             messages.info(request, "This item was removed from your cart.")
#             return redirect("core:cart")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("core:product", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("core:product", slug=slug)
#
# def remove_single_item_from_cart(request, slug):
#     product = get_object_or_404(models.Product, slug=slug)
#     order_qs = models.Order.objects.filter(
#         customer=request.user.customer,
#         complete=False
#     )
#     if order_qs.exists():
#         order = order_qs[0]
#         # check if the order item is in the order
#         if order.products.filter(product__slug=product.slug).exists():
#             order_item = models.OrderItem.objects.filter(
#                 product=product,
#                 customer=request.user.customer
#             )[0]
#             if order_item.quantity > 1:
#                 order_item.quantity -= 1
#                 order_item.save()
#             else:
#                 order.products.remove(order_item)
#             messages.info(request, "This item quantity was updated.")
#             return redirect("core:cart")
#         else:
#             messages.info(request, "This item was not in your cart")
#             return redirect("core:product", slug=slug)
#     else:
#         messages.info(request, "You do not have an active order")
#         return redirect("core:product", slug=slug)
