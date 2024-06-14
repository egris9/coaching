# from django.http import JsonResponse
from coach.api.queries.cart.helpers import check_for_cart, create_cart, get_cart_items


def show_products(user_id):
    # get cart items
    # check if user has a cart
    maybe_cart = check_for_cart(user_id)

    if maybe_cart["ok"] is False:
        total = 0
        maybe_cart["data"] = create_cart(user_id, total)
        return {"cart_items": [], "total": total}

    cart = maybe_cart["data"]

    cart_items = get_cart_items(cart)

    return {"cart_items": cart_items, "total": cart.total}
