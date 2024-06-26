from django.shortcuts import render
from coach.models import Training_session
from coach.forms import FilterForm

def session_filtre(request):
    form = FilterForm(request.GET)
    sessions = Training_session.objects.all()
    
    if form.is_valid():
        price_range = form.cleaned_data.get('price_range')
        sort_by = form.cleaned_data.get('sort_by')
        
        if price_range:
            if 'under_25' in price_range:
                sessions = sessions.filter(price__lt=25)
            if '25_to_50' in price_range:
                sessions = sessions.filter(price__gte=25, price__lte=50)
            if '50_to_100' in price_range:
                sessions = sessions.filter(price__gte=50, price__lte=100)
            if 'over_100' in price_range:
                sessions = sessions.filter(price__gt=100)
                
        if sort_by:
            if sort_by == 'popularity':
                sessions = sessions.order_by('-popularity')  # Assuming you have a popularity field
            elif sort_by == 'high_to_low':
                sessions = sessions.order_by('-price')
            elif sort_by == 'low_to_high':
                sessions = sessions.order_by('price')
    
    context = {
        'form': form,
        'sessions': sessions,
    }
    return render(request, 'session.html', context)
