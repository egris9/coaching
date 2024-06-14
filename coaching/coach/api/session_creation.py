from django.shortcuts import render
from coach.models import session_location, categorie

def session_creation(request):
    
    locations=session_location.objects.all()
    categories=categorie.objects.all()
    return render(
        request,
        'coach/session_creation.html',
        {'locations':locations, 'categorie':categories}
    )
