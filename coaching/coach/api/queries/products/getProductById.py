from coach.models import Product, ProductImages
from django.shortcuts import get_object_or_404


def get_product_by_id(id: int):
    product = get_object_or_404(Product, id=id)

    # Retrieve related images and variants
    images = ProductImages.objects.filter(product=product)


    return {
        "product": {
            "name": product.name,
            "description": product.description,
            "type": product.type,
            "id": product.id,
            "imgs": images,
        }
    }
