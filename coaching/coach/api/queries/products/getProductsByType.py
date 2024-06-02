from coach.models import Product


def get_products_by_type(type: str):
    data = (
        Product.objects.filter(type=type)
        .prefetch_related("productvariant_set")
        .prefetch_related("productimages_set")
    )

    products = []
    for p in data:
        url = None

        for img in p.productimages_set.all():
            if img.type == "main":
                url = img.urls

        variant = p.productvariant_set.first()
        products.append(
            {"name": p.name, "url": url, "price": variant.price, "id": p.id}
        )
    return {"products": products}
