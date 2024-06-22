from django.contrib import admin
from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderToProduct,
    ProductImages,
    Profile,
    Training_session,
    session_location,
    session_date,
    categorie,
    ProductVariant,
    Reviews,
)
# Register your models here.

admin.site.register(Product)
admin.site.register(Training_session)
admin.site.register(session_location)
admin.site.register(session_date)
admin.site.register(Profile)
admin.site.register(Reviews)
admin.site.site_header='Cancer'
admin.site.site_title='Cancer'

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderToProduct)
admin.site.register(ProductImages)
admin.site.register(ProductVariant)
admin.site.register(categorie)

