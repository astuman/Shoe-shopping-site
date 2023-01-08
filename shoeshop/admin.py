from django.contrib import admin
from .models import Customer, Product, Orders, Brand
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Orders, OrderAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand, BrandAdmin)


# Register your models here.
