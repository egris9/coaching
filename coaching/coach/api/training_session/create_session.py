from django.http import JsonResponse
from coach.api.queries.sessions.add_img import addimg
from coach.forms import ImageForm
from coach.models import Profile
from coach.models import Training_session,session_location
from django.shortcuts import  get_object_or_404, redirect

def add_session(request):
    if request.method != "POST":
        return JsonResponse(
            {"ok": False, "reason": "redirect", "url": "/shop"}
        )
    if request.user.is_authenticated == False:
        return redirect(
            '/signin'
        )
    profile= Profile.objects.get(user=request.user)
    if profile.type=='client':
        return redirect("/")
    
    if request.method == 'POST':
        location = session_location.objects.first()
        if profile is None:
            return JsonResponse({"ok":False , 'reason': 'profile_not_found'})
        
        combined_data = request.POST.copy()  # Make a copy to avoid modifying the original QueryDict
        combined_data['Profile'] = profile     
        combined_data['session_location'] = location     
        
        form = ImageForm(combined_data, request.FILES )
        if form.is_valid():
            instance= form.save()
            return JsonResponse({'ok': True, 'profile_id':profile.id, 'url':instance.img.url, 'session_id':instance.id}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=400)

def update_session_img(request):
    if request.method != "POST":
        return JsonResponse(
            {"ok": False, "reason": "redirect", "url": "/shop"}
        )
    if request.method == 'POST':
        session = get_object_or_404(Training_session, id=request.POST['session_id'])
        
        # profile = Profile.objects.filter(id='1').first()
        # if profile is None:
        # return JsonResponse({"ok":False , 'reason': 'profile_not_found'})
        
        combined_data = request.POST.copy()  # Make a copy to avoid modifying the original QueryDict
        combined_data['Profile'] = session.Profile     
    
        form = ImageForm(combined_data, request.FILES, instance=session )
        if form.is_valid():
             instance= form.save()
             return JsonResponse({'ok': True, 'message':'update_img','url':instance.img.url, 'session_id':instance.id}, status=200)
        else:
             return JsonResponse({'errors': form.errors}, status=400)

