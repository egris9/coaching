
from django.shortcuts import render,redirect
from django.utils import timezone
from datetime import datetime
from coach.models import Profile
from coach.api.queries.sessions.index import get_sessions_by_date, get_all_sessions_by_profile


def dashboard(request):
    
    if request.user.is_authenticated == False:
        return redirect(
            '/signin'
        )
    
    profile= Profile.objects.get(user=request.user)
    if profile.type=='client':
        return redirect("/")
    
    date_filter_start_str = request.GET.get('filter-by-period-start', None)
    date_filter_end_str = request.GET.get('filter-by-period-end', None)

    if date_filter_start_str and date_filter_end_str:

        date_filter_start = timezone.make_aware(datetime.strptime(date_filter_start_str, '%Y-%m-%d'))
        date_filter_end = timezone.make_aware(datetime.strptime(date_filter_end_str, '%Y-%m-%d'))
        sessions = get_sessions_by_date(profile=profile, date_filter_start=date_filter_start, date_filter_end=date_filter_end)

        return render(
        request,
        'coach/dashboard.html'
        ,{'sessions': sessions, "filter_trigger": request.GET.get('filter-trigger', None)}
    )
  
    session = get_all_sessions_by_profile(profile)
    full_name= request.user.first_name+' '+request.user.last_name
    img=Profile.objects.filter(user=request.user).first().image.url   

    return render(
        request,
        'coach/dashboard.html'
        ,{'sessions': session, "filter_trigger": "all", "full_name":full_name , "img":img}
    )