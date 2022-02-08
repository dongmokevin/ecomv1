from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('store', views.StoreProductListView.as_view(), name='store'),
    path('store/<slug:slug>', views.ProductDetailView.as_view(), name='product'),
    # path('store/<slug:slug>', views.product_detail, name='product'),
    path('products/add', views.ProductCreateView.as_view(), name='add-product'),
    # path('cart', views.CartView.as_view(), name='cart'),
    #path('cart', views.cart, name='cart'),
    # path('checkout', views.checkout, name='checkout'),
    # path('checkout', views.CheckoutView.as_view(), name='checkout'),
    # path('update_item', views.updateItem, name='update_item'),
    #
    # path('add-to-cart/<slug>', views.add_to_cart, name='add-to-cart'),
    # path('remove-from-cart/<slug>', views.remove_from_cart, name='remove-from-cart'),
    # path('remove_single_item_from_cart/<slug>', views.remove_single_item_from_cart, name='remove_single_item_from_cart'),

    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
]
