from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from coach.models import Profile, Training_session, session_date, User, Reviews


def reviews(request, session_id):

    if request.user.is_authenticated == False:
        return JsonResponse({"redirect": "/signin", "ok": False})
    title = request.POST.get("title")
    description = request.POST.get("description")
    stars = request.POST.get("stars")
    session = Training_session.objects.get(id=session_id)
    Reviews.objects.create(
        title=title,
        description=description,
        stars=stars,
        sesison=session,
        user=request.user,
    )

    return JsonResponse({"ok": True})
