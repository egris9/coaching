from django.shortcuts import render, redirect

def sign_in(request):
    
    return render(
        request,
        "coach/home.html",
    
    )