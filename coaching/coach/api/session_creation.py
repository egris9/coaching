from django.shortcuts import render




def session_creation(request):
    
    return render(
        request,
        'coach/session_creation.html'
    )
