from datetime import datetime, timedelta
from django.db.models import Count, Q
from django.shortcuts import render
from coach.models import Training_session, OrderToProduct
from coach.api.queries.sessions.index import session_meta_data

def get_current_week():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

def top_sessions():
    # Get the start and end dates for the current week
    start_of_week, end_of_week = get_current_week()
    # Annotate and order the sessions based on the number of orders in the current week
    sessions = (Training_session.objects
                .annotate(num_orders=Count('orders_training_session', filter=Q(orders_training_session__date__range=(start_of_week, end_of_week))))
                .filter(num_orders__gt=0)
                .order_by('-num_orders')[:3])
    session_meta = []
    for s in sessions:
        session_meta.append(session_meta_data(s))


    return session_meta
