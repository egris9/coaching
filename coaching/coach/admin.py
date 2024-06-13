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
    
)
# Register your models here.

admin.site.register(Product)
admin.site.register(Training_session)
admin.site.register(session_location)
admin.site.register(session_date)
admin.site.register(Profile)
admin.site.site_header='APOSTEl PANEL'
admin.site.site_title='APOSTEl PANEL'

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderToProduct)
admin.site.register(ProductImages)

