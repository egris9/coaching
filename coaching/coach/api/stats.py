from django.shortcuts import render


def stats(request):
    
    return render(request,"coach/stats.html")
