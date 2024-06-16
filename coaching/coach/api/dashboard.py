
from django.shortcuts import render,redirect
from coach.models import Profile,Training_session,session_date




def dashboard(request):
    
    if request.user.is_authenticated == False:
        return redirect(
            '/signin'
        )
    profile= Profile.objects.get(user=request.user)
    if profile.type=='client':
        return redirect("/")
    
    data=Training_session.objects.filter(Profile=profile)
     
  
    session = []
    for p in data:
        first_date=session_date.objects.filter(session=p).first()
        last_date=session_date.objects.filter(session=p).last()

        session.append(
            {"first_date": first_date, "last_date": last_date,'name':p.name,'small_sum':p.small_sum, 'categorie':p.categorie,'img':p.img ,'type':p.type}
        )  

    return render(
        request,
        'coach/dashboard.html'
        ,{'sessions': session}
    )
