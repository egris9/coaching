from django.shortcuts import render
from coach.models import session_location

def session_creation(request):
    
    locations=session_location.objects.all()
    return render(
        request,
        'coach/session_creation.html',
        {'locations':locations}
    )
