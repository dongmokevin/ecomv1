from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from datetime import date

from core.models import Product

from .basket import Basket

import json
from django.http import HttpResponseRedirect
import urllib.parse


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'cart.html', {'basket': basket })


def send_message(request):
    basket = Basket(request)
    # print('this is GOOOOOo==========================')
    order = basket.basket
    orderList = list(order.values())
    go = json.dumps(orderList, indent=4)
    orderStr = f"""*From Yaounde Market*

Your Order on {date.today()}

Your total order items in *cart ({basket.__len__()})*

Items:
"""

    for dic in orderList:
        orderStr = orderStr + '\n'
        for key in dic:
            orderStr = orderStr + f'\t{key} : {dic[key]}\n'

    baskettotal = 'XAF ' + str(basket.get_total_price())

    billstr = f"""
*Total\t{baskettotal}*
    """
    orderStr = orderStr + billstr
    # print(orderStr)
    orderUrl = urllib.parse.quote(orderStr)
    # print(orderUrl)
    return HttpResponseRedirect("https://wa.me/+237657131677?text=" + orderUrl)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        product_price = basket.product_price(product=product_id)
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal, 'product_price': product_price})
        return response
