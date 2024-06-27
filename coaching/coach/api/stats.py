from django.shortcuts import render
from django.db.models import Count,Sum
from django.db.models.functions import TruncMonth
from coach.models import OrderToProduct
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Count, Q
from datetime import datetime, timedelta




def stats(request):

    return render(request,"coach/stats.html")
def participent_by_coach(request):
    
    training_session = OrderToProduct.objects.filter(training_session__Profile=request.user.profile).annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id')).order_by('month')
    #training_session = OrderToProduct.objects
    print(training_session.count())
    participent_by_month=[]
    for session in training_session.all() :
        
        month_name = session['month'].strftime('%B')
        
        participent_by_month.append({
            'count':session['count'],
            'month':month_name
        })


    return JsonResponse({'participent_by_month':participent_by_month})
    
def revenue_by_session(request):
    
    training_session = OrderToProduct.objects.filter(training_session__Profile=request.user.profile,product=None).annotate(month=TruncMonth('date')).values(
        "training_session__id","training_session__name" ,'month').annotate(total_amount=Sum('price')).annotate(count=Count('id')).order_by('month')
    total_sum_price = OrderToProduct.objects.filter(training_session__Profile=request.user.profile,product=None).annotate(
    month=TruncMonth('date')
            ).values(
     'month'
            ).annotate(
    total_price=Sum('price')
            ).order_by(
    'month'
            )
    # price in total_sum_price :
       # total_each_month.append(price['total_sum'])
        
    
    revenue=[]
    for session in training_session.all() :
        
        month_name = session['month'].strftime('%b')
        
        revenue.append({
            'total':session['total_amount'],
            'name':session['training_session__name'],
            'month':month_name,
            
        })

        
    total_each_month = []
    for month_data in total_sum_price:
        month_name = month_data['month'].strftime('%b')
        total_each_month.append({
            'month': month_name,
            'total_price': month_data['total_price']
        })
    
    
    return JsonResponse({'revenue_by_session':revenue,'total_each_month':total_each_month})



def get_current_week():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week

def top_sessions(request):
    # Get the start and end dates for the current week
    start_of_week, end_of_week = get_current_week()
    # Annotate and order the sessions based on the number of orders in the current week
    sessions = OrderToProduct.objects.filter(training_session__Profile=request.user.profile,product=None,date__range=(
            start_of_week, end_of_week)).values('training_session__id','training_session__name').annotate(
            total_amount=Sum('price'),  num_orders=Count('training_session')).filter(num_orders__gt=0).order_by('-num_orders')[:5]


    session_meta = []
    for s in sessions:
        session_meta.append({'revenues':s['total_amount'],'participent_count':s['num_orders'],'name':s['training_session__name']})

    return JsonResponse({'payload':session_meta})