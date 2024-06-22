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
    reviews_list=[]
    
    stars_count=0
    stars_average=0
    sum_stars=0
    
    if reviews.exists():
        for review in reviews.all():
            reviews_list.append({'title':review.title,'comment':review.comment,'stars':review.stars,
                                "full_name": review.user.first_name + " " +review.user.last_name,"url": Profile.objects.filter(user=review.user).first().image.url
                                })
            
            sum_stars= review.stars+sum_stars
        stars_count= reviews.count()
        stars_average= sum_stars/stars_count
        print(stars_average,stars_count)
    
        
        

        
         
    return JsonResponse({'ok':True,'reviews':reviews_list,'reviews_count':stars_count,'stars_average':stars_average})


    
    
    