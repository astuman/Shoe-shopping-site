from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    """Customer model"""
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    """Product model"""
    name=models.CharField(max_length=40)
    brand_name= models.ForeignKey("Brand", on_delete=models.CASCADE,null=False)
    category= models.ForeignKey('Category', on_delete=models.CASCADE,null=True)
    size=models.PositiveIntegerField()
    quantity=models.CharField(max_length=10, null=True, blank=True)
    product_image= models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description=models.TextField({'rows': 3, 'cols': 30})
    def __str__(self):
        return self.name


class Orders(models.Model):
    """Orders model"""
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Brand(models.Model):
    """Brand model"""
    brand_name = models.CharField(max_length=40)
    def __str__(self):
        return self.brand_name

class Category(models.Model):
    """category Model"""
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category