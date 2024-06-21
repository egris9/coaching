from django.http import JsonResponse
from django.shortcuts import redirect
from coach.api.queries.cart.helpers import update_quantity


def update_item_quantity(request):
    if request.method != "POST":
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/shop"}
        )

    if request.user.is_authenticated == False:
        return JsonResponse(
            {"ok": True, "status": 200, "action": "redirect", "url": "/login"}
        )

    import json

    #Il extrait les données JSON du corps de la requête, décodées en UTF-8, et les stocke dans la variable data
    data = json.loads(request.body.decode("utf-8"))

    isUpdated = update_quantity(
        id=data["id"], quantity=data["quantity"], cart_total=data["cartTotal"]
    )

    if isUpdated["ok"] is False:
        return JsonResponse({"ok": False, "cause": isUpdated["cause"], "status": 404})

    return JsonResponse(
        {"ok": True, "status": 200, "action": "update", "item": isUpdated["data"]}
    )
