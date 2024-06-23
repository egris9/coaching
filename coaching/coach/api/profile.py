from django.shortcuts import render,redirect
from coach.models import Order,Profile
from coach.forms import Editprofileform,Editimageprofileform
from coach.api.queries.sessions.index import get_all_sessions_by_profile_client,get_all_sessions_by_profile_client_date
from django.utils import timezone
from datetime import datetime


def profile(request):
    orders = Order.objects.all().prefetch_related("ordertoproduct_set")
    order_data = []
    full_name= request.user.first_name+' '+request.user.last_name
    img=Profile.objects.filter(user=request.user).first().image.url   

    for order in orders:
            for order_item in order.ordertoproduct_set.all():
                if order_item.training_session:
                    training_session_name = order_item.training_session.name
                else:
                    training_session_name = "No Session"
                order_data.append({
                "name":order_item.product_name,
                "price":order_item.price,
                "first_name":order.first_name,
                "last_name":order.last_name,
                "email":order.email,
                "order_total":order.order_total,
                "training_session":training_session_name,
            })

    if request.method == "POST":
         form = Editprofileform (data=request.POST, instance=request.user)
         if form.is_valid():
              form.save()
              instance= Editimageprofileform(request.POST, request.FILES , instance=request.user.profile )
              if instance.is_valid() :
                   instance.save()
                   return redirect("/profile")
              
    session = get_all_sessions_by_profile_client(request.user.profile)

    date_filter_start_str = request.GET.get('filter-by-period-start', None)
    date_filter_end_str = request.GET.get('filter-by-period-end', None)

    if date_filter_start_str and date_filter_end_str:

        date_filter_start = timezone.make_aware(datetime.strptime(date_filter_start_str, '%Y-%m-%d'))
        date_filter_end = timezone.make_aware(datetime.strptime(date_filter_end_str, '%Y-%m-%d'))
        sessions = get_all_sessions_by_profile_client_date(profile=request.user.profile, date_filter_start=date_filter_start, date_filter_end=date_filter_end)

        return render(
        request,
        'coach/profile.html'
        ,{'sessions': sessions, "filter_trigger": request.GET.get('filter-trigger', None),'product_data': order_data ,"full_name":full_name , "img":img}
    )
        
    return render(request, 'coach/profile.html', {'product_data': order_data ,"full_name":full_name , "img":img, 'sessions': session})