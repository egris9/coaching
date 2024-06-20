from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from coach.models import Profile, Training_session,session_date,User




def pop_up(request,session_id):
    session = get_object_or_404(Training_session, id=session_id)
    first_date=session_date.objects.filter(session=session).first()
    last_date=session_date.objects.filter(session=session).last()
    last_date=last_date.date.strftime("%d %B")
    first_date=first_date.date.strftime("%d %B")
    
    coach=session.Profile.user.first_name +" "+ session.Profile.user.last_name
    print(coach)
    
    return JsonResponse({"first_date": first_date,'coach':coach, "last_date": last_date,'description':session.description,'price':session.price,'name':session.name,'start_time':session.start_time.strftime("%H:%M"),
     'end_time':session.end_time.strftime("%H:%M"),'location':session.location.location,'participent':session.participant_limit,'categorie':session.categorie,'type':session.type,'status': 'success'})