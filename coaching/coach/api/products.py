from django.shortcuts import render, redirect

def products(request):
    
    return render(
        request,
        "coach/products.html",
       
    )