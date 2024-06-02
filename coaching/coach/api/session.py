from django.shortcuts import render, redirect

def session(request):
    
    return render(
        request,
        "coach/session.html",
       
    )