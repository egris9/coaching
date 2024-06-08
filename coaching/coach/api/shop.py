from django.shortcuts import render
from coach.api.queries.products.getAllProducts import get_all_products
from coach.api.queries.products.getProductsByType import get_products_by_type


def shop(request):
    products = {}

    filter = request.GET.get("filter", "")

    if filter == "dumbelle" or filter == "weight" or filter == "iron bar":
        products = get_products_by_type(filter)
    else:
        products = get_all_products()

    return render(request, "coach/shop.html", {**products, "filter": filter})
