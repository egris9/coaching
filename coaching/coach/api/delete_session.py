from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from coach.models import Profile, Training_session

def delete_session(request, session_id):
    session = get_object_or_404(Training_session, id=session_id)
    if request.method == 'POST':
        session.delete()
        return JsonResponse({'message': 'Session deleted successfully', 'status': 'success'})
    return JsonResponse({'message': 'Invalid request method', 'status': 'error'}, status=400)
