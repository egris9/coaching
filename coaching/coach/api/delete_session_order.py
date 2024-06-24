from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from coach.models import Profile, Training_session,OrderToProduct

def delete_session_order(request, order_id):
    if request.method == 'POST':
        order = OrderToProduct.objects.filter(id=order_id)
        order.delete()
        return JsonResponse({'message': 'Session deleted successfully', 'status': 'success'})
    return JsonResponse({'message': 'Invalid request method', 'status': 'error'}, status=400)