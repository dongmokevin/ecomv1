from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, DetailView

from basket.basket import Basket

from .models import Order, OrderItem
from account.models import UserBase
from .forms import CheckoutFormView, MessageForm, ContactForm

# from django.http import JsonResponse
# from .utils import send_whatsapp_message

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                address2='add2', total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

class CreateOrderView(CreateView):
    model = Order
    form_class = CheckoutFormView
    template_name = 'checkout.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class MessageOrderView(DetailView):
    model = UserBase
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if request.is_ajax():
            if form.is_valid():
                message_to = self.get_object().phone_number
                body = form.cleaned_data.get('body')
                send_whatsapp_message(body, message_to)
                return JsonResponse({'body':body})
            return redirect('core:store')
        return redirect('core:store')
