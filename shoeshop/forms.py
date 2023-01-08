from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    """To take information about name, username and password """
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class CustomerForm(forms.ModelForm):
    """To take information about address, mobile and picture"""
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']


class ProductForm(forms.ModelForm):
    """product information"""
    class Meta:
        model = models.Product
        fields = [
            'name',
            'brand_name',
            'category',
            'size',
            'quantity',
            'price',
            'description',
            'product_image']


class AddressForm(forms.Form):
    """addres of shipment """
    Email = forms.EmailField()
    Mobile = forms.IntegerField()
    Address = forms.CharField(max_length=500)


class OrderForm(forms.ModelForm):
    """for updating status of order"""
    class Meta:
        model = models.Orders
        fields = ['status']


class brandForm(forms.ModelForm):
    """for brand form"""
    class Meta:
        model = models.Brand
        fields = ['brand_name']


class categoryForm(forms.ModelForm):
    """for category form"""
    class Meta:
        model = models.Category
        fields = ['category']
