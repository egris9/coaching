from coach.models import Product,OrderToProduct
from django.db.models import Count

def popular_products():

    popular_products = Product.objects.annotate(num_orders=Count('orders_product')).order_by('-num_orders')[:5].prefetch_related("productvariant_set").prefetch_related(
            "productimages_set"
        )

    products = []
    for p in popular_products:
        url = None

        for img in p.productimages_set.all():
            if img.type == "main":
                 url = img.urls

        variant = p.productvariant_set.first()
        products.append(
            {"name": p.name, "url": url, "price": variant.price if variant else None, "id": p.id}
        )
    return products
