from django.http import JsonResponse
from django.shortcuts import redirect
from coach.api.queries.cart.helpers import delete_cart_item


def delete_cart_item_handler(request):
    if request.method != "POST":
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/shop"}
        )

    if request.user.is_authenticated == False:
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/login"}
        )

    import json

    #Il extrait les données JSON du corps de la requête, décodées en UTF-8, et les stocke dans la variable data.
    data = json.loads(request.body.decode("utf-8"))

    isDeleted = delete_cart_item(id=data["id"])

    if isDeleted["ok"] is False:
        return JsonResponse({"ok": False, "cause": isDeleted["cause"], "status": 404})

    return JsonResponse(
        {"ok": True, "status": 200, "action": "delete", "data": isDeleted["data"]}
    )
