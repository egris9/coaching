from django.http import JsonResponse
from django.shortcuts import redirect
from coach.models import Order, OrderToProduct
from coach.api.queries.cart.helpers import (
    get_cart_by_item_id,
    get_cart_items_with_products,
    empty_cart,
)


def add_order_handler(request):
    if request.method != "POST":
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/shop"}
        )

    if request.user.is_authenticated == False:
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/login"}
        )

    import json

    data = json.loads(request.body.decode("utf-8"))["data"]

    maybe_cart = get_cart_by_item_id(id=data["cart_item_id"])

    if maybe_cart["ok"] is False:
        return JsonResponse({"ok": False, "status": 404, "cause": maybe_cart["cause"]})

    cart_items = get_cart_items_with_products(cart=maybe_cart["cart"])

    new_order = Order(
        first_name=data["first_name"],
        last_name=data["last_name"],
        email=data["email"],
        address=data["address"],
        cart_name=data["cart_name"],
        exp=data["exp"],
        cvv=data["cvv"],
        order_total=maybe_cart["cart"].total,
        user_id=request.user.id,
    )
    new_order.save()

    # move cart items to orderToProduct table
    for item in cart_items:
        OrderToProduct.objects.create(
            order_id=new_order,
            product=item["product"],
            product_name=item["name"],
            quantity=item["quantity"],
            price=item["price"],
            type=item["type"],
            training_session=item["training_session"],
        )

    empty_cart(maybe_cart["cart"])

    maybe_cart["cart"].total = 0
    maybe_cart["cart"].save()

    return JsonResponse({"ok": True, "status": 200})
