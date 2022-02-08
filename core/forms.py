from django.forms import ModelForm
from .models import Product
# class CheckoutFormView(forms.Form):
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Address Line 1'
#     }))
#     address_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={
#         'placeholder': 'Address Line 2 (optional)' }))
#     town = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Town / City' }))
#     zip_code = forms.CharField(required=False, widget=forms.TextInput(attrs={
#         'placeholder': 'ZIP / Postcode' }))
#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Mobile Phone',
#         'type': 'tel' }))
#     notes = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Order Notes (optional)',
#         'rows' : 5
#     }),required=False)

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'generic_name', 'price', 'decription', 'image',]
