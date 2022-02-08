from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('add-order/', views.CreateOrderView.as_view(), name='create-order'),
    # path('send/<pk>', views.MessageOrderView.as_view(), name='send-message'),
]
