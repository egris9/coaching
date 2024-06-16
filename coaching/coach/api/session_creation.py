from django.shortcuts import render,redirect
from coach.models import session_location,Profile


def session_creation(request):
    
    locations=session_location.objects.all()
    
    if request.user.is_authenticated == False:
        return redirect(
            '/signin'
        )
    profile= Profile.objects.get(user=request.user)
    if profile.type=='client':
        return redirect("/")
    
    return render(
        request,
        'coach/session_creation.html',
        {'locations':locations}
    )
