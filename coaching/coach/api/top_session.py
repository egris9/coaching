from datetime import datetime, timedelta
from django.db.models import Count
from django.shortcuts import render
from coach.models import Training_session, Order

def get_current_week():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

def top_sessions(request):
    # Get the start and end dates for the current week
    start_of_week, end_of_week = get_current_week()

    # Annotate and order the sessions based on the number of orders in the current week
    sessions = (Training_session.objects
                .annotate(num_orders=Count('orders', filter=Order.objects.filter(date__range=(start_of_week, end_of_week))))
                .order_by('-num_orders')[:3])

    # Pass the sessions to the template context
    context = {'sessions': sessions}
    return render(request, 'your_template.html', context)
