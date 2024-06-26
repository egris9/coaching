from django.http import JsonResponse
from coach.models import Product
from coach.api.queries.products.getAllProducts import get_all_products

def product_list(request):
    products = get_all_products()

    products_set = []

    for p in products['products']:
        products_set.append({**p, "url": p["url"].url})

    return JsonResponse({"products": products_set}, safe=False)
