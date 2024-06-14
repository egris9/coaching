from django.shortcuts import render, redirect
from coach.api.queries.products.getProductById import get_product_by_id
from coach.api.queries.products.popularProducts import popular_products



def products(request, id):
    product = get_product_by_id(id)
    products = popular_products()
    return render(
        request,
        "coach/products.html",{**product, "popular_products": products}
       
    )