from django.shortcuts import render, redirect

def shop(request):
    
    return render(
        request,
        "coach/shop.html",
       
    )