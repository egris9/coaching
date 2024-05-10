from django.shortcuts import render, redirect

def sign_up(request):
    
    return render(
        request,
        "coach/home.html",
       
    )