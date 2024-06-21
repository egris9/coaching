from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from coach.models import Profile, Training_session, session_date, User, Reviews
import json

def reviews(request, session_id):

    if request.user.is_authenticated == False:
        return JsonResponse({"redirect": "/signin", "ok": False})
   

    data = json.loads(request.body.decode("utf-8"))
    title = data["title"]
    description = data["description"]
    stars = data["stars"]
    session = Training_session.objects.get(id=session_id)
    full_name= request.user.first_name+' '+request.user.last_name
    img=Profile.objects.filter(user=request.user).first().image.url   
    Reviews.objects.create(
        title=title,
        comment=description,
        stars=stars,
        session=session,
        user=request.user,
    )

    return JsonResponse({"ok": True,'full_name':full_name,'img':img})
def get_sessions_reviews(request,session_id):
    reviews=Reviews.objects.filter(session__id=session_id)
    return JsonResponse({'ok':True,'reviews':reviews})
    
    
    