from coach.models import Product, ProductImages,ProductVariant
from django.shortcuts import get_object_or_404


def get_product_by_id(id: int):
    product = get_object_or_404(Product, id=id)

    # Retrieve related images and variants
    images = ProductImages.objects.filter(product=product)
    variants = ProductVariant.objects.filter(product=product)


    first_variant = variants.first()

    return {
        "product": {
            "name": product.name,
            "price": first_variant.price,
            "description": product.description,
            "type": product.type,
            "id": product.id,
            "imgs": images,
            "varients": variants,
        }
    }
