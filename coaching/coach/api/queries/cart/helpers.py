from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from coach.models import CartItem
from coach.models import Cart, Product


def check_for_cart(user_id):
    try:
        cart = Cart.objects.get(user__id=user_id)
        return {"ok": True, "data": cart}

    except Cart.DoesNotExist:
        return {"ok": False, "data": None}


def check_for_item(cart, product_id):
    try:
        item = CartItem.objects.get(
            cart_id=cart, product__id=product_id
        )

        return {"ok": True, "data": item}

    except CartItem.DoesNotExist:
        return {"ok": False, "data": None}


def create_cart(user_id, total):
    user = User.objects.get(id=user_id)
    cart = Cart.objects.create(total=total, user=user)

    return cart


def create_cart_item(cart, data):
    try:
        product = Product.objects.get(id=data["productId"])
        item = CartItem.objects.create(
            quantity=data["quantity"],
            price=data["price"],
            cart_id=cart,
            product=product,
        )
        return {"ok": True, "data": item}

    except Product.DoesNotExist:
        return {"ok": False, "cause": "product"}


def update_quantity(id, quantity, cart_total):
    try:
        cart_item = CartItem.objects.get(id=id)
        # Update the quantity
        cart_item.quantity = quantity
        # Save the changes
        cart_item.save()
        # update cart total according to quantity changes
        cart_item.cart_id.total = cart_total
        cart_item.cart_id.save()

        return {
            "ok": True,
            "action": "update",
            "data": {
                "id": cart_item.id,
                "quantity": cart_item.quantity,
                "price": cart_item.price,
            },
        }
    except CartItem.DoesNotExist:
        return {"ok": False, "cause": "not found"}


def empty_cart(cart):
    CartItem.objects.filter(cart_id=cart).delete()


def get_cart_items(cart):
    items = CartItem.objects.filter(cart_id=cart).prefetch_related("product")

    cart_items = []

    for item in items.all():
        for img in item.product.productimages_set.all():
            if img.type == "main":
                cart_items.append(
                    {
                        **model_to_dict(item),
                        "img": img.urls,
                        "type": item.product.type,
                        "name": item.product.name,
                    }
                )

    return cart_items


def get_cart_items_with_products(cart):
    items = CartItem.objects.filter(cart_id=cart).prefetch_related("product")

    cart_items = []

    for item in items.all():
        for img in item.product.productimages_set.all():
            if img.type == "main":
                cart_items.append(
                    {
                        **model_to_dict(item),
                        "img": img.urls,
                        "type": item.product.type,
                        "name": item.product.name,
                        "product": item.product,
                    }
                )

    return cart_items


def delete_cart_item(id):
    try:
        cart_item = CartItem.objects.get(id=id)
        # update cart total
        cart_total = cart_item.cart_id.total - (cart_item.price * cart_item.quantity)
        cart_item.cart_id.total = cart_total
        cart_item.cart_id.save()

        # delete cart item
        cart_item.delete()

        return {"ok": True, "action": "delete", "data": {"cart_total": cart_total}}
    except CartItem.DoesNotExist:
        return {"ok": False, "cause": "not found"}


def get_cart_by_item_id(id):
    try:
        cart_item = CartItem.objects.get(id=id)

        return {"ok": True, "cart": cart_item.cart_id}
    except CartItem.DoesNotExist:
        return {"ok": False, "cause": "not found"}
