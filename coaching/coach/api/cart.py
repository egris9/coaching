from django.shortcuts import render, redirect
from coach.api.queries.cart.showProducts import show_products


def cart(request):
    if request.user.is_authenticated is False:
        return redirect("/login")

    cart_items = show_products(request.user.id)

    # Si la méthode de requête n'est pas POST, afficher simplement le formulaire
    return render(request, "coach/cart.html", {**cart_items})
