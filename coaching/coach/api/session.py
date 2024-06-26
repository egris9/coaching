from django.shortcuts import render, redirect
from coach.models import Training_session,categorie
from coach.forms import FilterForm
from coach.api.queries.sessions.index import  format_sessions_response
from django.db.models import Count



def session(request):
    allow_filter = request.GET.get('allow_filter', None)
    sessions = Training_session.objects.all()
    if allow_filter : 
        form = FilterForm(request.GET)
        if form.is_valid():
            price_range = form.cleaned_data.get('price_range')
            sort_by = form.cleaned_data.get('sort_by')
            category = request.GET.get('category')
            session_type = form.cleaned_data.get('session_type')
            
            if price_range:
                if 'under_25' in price_range:
                    sessions = sessions.filter(price__lt=25)
                if '25_to_50' in price_range:
                    sessions = sessions.filter(price__gte=25, price__lte=50)
                if '50_to_100' in price_range:
                    sessions = sessions.filter(price__gte=50, price__lte=100)
                if 'over_100' in price_range:
                    sessions = sessions.filter(price__gt=100)

            if category:
                sessions = sessions.filter(categorie=category)

            if session_type:
                sessions = sessions.filter(type__iexact=session_type)
                    
            if sort_by:
                if sort_by == 'popularity':
                    sessions = sessions.annotate(num_orders=Count('orders_training_session')).order_by('-num_orders')  # Assuming you have a popularity field
                elif sort_by == 'high_to_low':
                    sessions = sessions.order_by('-price')
                elif sort_by == 'low_to_high':
                    sessions = sessions.order_by('price')
    categories = []
    for c in categorie.objects.all():
        categories.append({'name':c.name})
    context = {
        'sessions': format_sessions_response(sessions),
        'categories' : categories,

    }
    return render(
        request,
        "coach/session.html",
        context
    )