from django.http import JsonResponse
from coach.api.queries.cart.helpers import (
    check_for_item,
    create_cart_item,
    check_for_cart,
    create_cart,
)


def add_to_cart(request):
    if request.method != "POST":
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/shop"}
        )

    if request.user.is_authenticated == False:
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/signin"}
        )

    import json

    data = json.loads(request.body.decode("utf-8"))
    user_id = request.user.id

    # check if user has a cart
    maybe_cart = check_for_cart(user_id)

    if maybe_cart["ok"] is False:
        total = 0
        maybe_cart["data"] = create_cart(user_id, total)

    cart = maybe_cart["data"]

    maybe_item = check_for_item(
        cart=cart,
        product_id=data["productId"],
        product_type=data["product_type"]
    )

    # check if it is the same product with the same
    # flavor and serving size if so increase
    # the quantity else add the item
    # into the cart
    if maybe_item["ok"]== True:
        item = maybe_item["data"] 
        if data["product_type"] == "session" :
            return JsonResponse({"ok": True, "status": 200, "action": "nothing"})
        if item.quantity == data["quantity"]:
            return JsonResponse({"ok": True, "status": 200, "action": "nothing"})

        # change the total of the cart depending on the price and quantity
        previous_item_total = item.price * item.quantity
        new_item_total = data["price"] * data["quantity"]
        cart.total = (cart.total - previous_item_total) + new_item_total
        cart.save()
        # increase qty
        item.quantity = data["quantity"]
        item.save()
        return JsonResponse({"ok": True, "status": 200, "action": "update"})

    maybe_new_item = create_cart_item(cart=maybe_cart["data"], data=data,product_type=data["product_type"])

    if maybe_new_item["ok"] is False:
        return JsonResponse(
            {"ok": False, "cause": maybe_new_item["cause"], "status": 500}
        )

    new_item = maybe_new_item["data"]
    # increase cart total
    cart = maybe_cart["data"]
    cart.total = cart.total + (new_item.price * new_item.quantity)
    cart.save()

    return JsonResponse(
        {
            "ok": True,
            "status": 200,
            "action": "create",
            "item": {
                "quantity": new_item.quantity,
                "price": new_item.price,
                "id": new_item.id,
                "productId": new_item.product.id if new_item.type == 'accessory' else None,
                "type": new_item.type,
                "sessionId" : new_item.training_session.id if new_item.type == 'session' else None
            },
        }
    )
