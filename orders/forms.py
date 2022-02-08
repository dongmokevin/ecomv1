from django import forms
from django.forms import ModelForm
from .models import Order
from account.models import UserBase

class CheckoutFormView(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        exclude = ['user', 'total_paid',]
    # full_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Your Full Name' }))
    # address1 = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Address Line 1'
    # }))
    # address_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={
    #     'placeholder': 'Address Line 2 (optional)' }))
    # city = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Town / City' }))
    # post_code = forms.CharField(required=False, widget=forms.TextInput(attrs={
    #     'placeholder': 'ZIP / Postcode' }))
    # phone = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Mobile Phone',
    #     'type': 'tel' }))
    # # notes = forms.CharField(widget=forms.Textarea(attrs={
    #     'placeholder': 'Order Notes (optional)',
    #     'rows' : 5
    # }),required=False)

class ContactForm(forms.ModelForm):
    class Meta:
        model = UserBase
        fields = '__all__'

class MessageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Order Notes (optional)',
        'rows' : 5
    }),required=False)
