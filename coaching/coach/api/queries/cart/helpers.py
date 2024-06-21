from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from coach.models import CartItem
from coach.models import Cart, Product,Training_session


def check_for_cart(user_id):
    try:
        cart = Cart.objects.get(user__id=user_id)
        return {"ok": True, "data": cart}

    except Cart.DoesNotExist:
        return {"ok": False, "data": None}


def check_for_item(cart, product_id,product_type):
    try:

        item = None
        if product_type == 'accessory':
            item = CartItem.objects.get(
            cart_id=cart, product__id=product_id
            )
        else:
            item = CartItem.objects.get(
            cart_id=cart, training_session__id=product_id
            )

        return {"ok": True, "data": item}

    except CartItem.DoesNotExist:
        return {"ok": False, "data": None}


def create_cart(user_id, total):
    user = User.objects.get(id=user_id)
    cart = Cart.objects.create(total=total, user=user)

    return cart


def create_cart_item(cart, data,product_type):
    try:
        
        cart_item = None
        if product_type == 'accessory':
            item = Product.objects.get(id=data["productId"])
            cart_item = CartItem.objects.create(
            quantity=data["quantity"],
            price=data["price"],
            cart_id=cart,
            product=item,
            type=product_type,

        )
        else:
            item = Training_session.objects.get(
                id=data["productId"]
            )
            cart_item = CartItem.objects.create(
            quantity=data["quantity"],
            price=data["price"],
            cart_id=cart,
            training_session=item,
        )

        return {"ok": True, "data": cart_item}

    except Product.DoesNotExist:
        return {"ok": False, "cause": "product"}
    except Training_session.DoesNotExist:
        return {"ok": False, "cause": "session"}



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
        if(item.type == "accessory"):
            for img in item.product.productimages_set.all():
                if img.type == "main":
                    cart_items.append(
                        {
                            **model_to_dict(item),
                            "img": img.urls,
                            "type": item.product.type,
                            "name": item.product.name,
                            "cart_item_type":"accessory",
                        }

                    )
        else:
            cart_items.append(
                {
                    **model_to_dict(item),
                    "cart_item_type":"session",
                }
            )
 

    return cart_items


def get_cart_items_with_products(cart):
    items = CartItem.objects.filter(cart_id=cart).prefetch_related("product")

    cart_items = []

    for item in items.all():
        if(item.type == "accessory"):
            for img in item.product.productimages_set.all():
                if img.type == "main":
                    cart_items.append(
                        {
                            **model_to_dict(item),
                            "img": img.urls,
                            "type": item.product.type,
                            "name": item.product.name,
                            "cart_item_type":"accessory",
                            "product":item.product,
                        }

                    )
        else:
            cart_items.append(
                {
                    **model_to_dict(item),
                    "cart_item_type":"session",
                    "training_session":item.training_session,
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
