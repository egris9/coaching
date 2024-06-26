from coach.models import Profile,Training_session,session_date,Order,Reviews
from datetime import datetime, date
from django.db.models import  Exists, Q, OuterRef


def format_sessions_response(sessions):
    session = []
    for p in sessions:
        first_date=session_date.objects.filter(session=p).first()
        last_date=session_date.objects.filter(session=p).last()
        star_rating = get_session_rating(p.id)

        today = date.today()
        start_datetime = datetime.combine(today, p.start_time )
        end_datetime = datetime.combine(today, p.end_time)
        duration = end_datetime - start_datetime 
        duration_hours = duration.total_seconds() / 3600  
        int_duration_hours = int(duration_hours)
        coach_first_name = p.Profile.user.first_name
        coach_last_name = p.Profile.user.last_name
        coach_img = p.Profile.image

        session.append(
            {"id":p.id,"first_date": first_date, "last_date": last_date,'name':p.name,'small_sum':p.small_sum, 'categorie':p.categorie,'img':p.img ,'type':p.type,'price':p.price,'location':p.location.location,'participant_limit':p.participant_limit,"start_time": p.start_time, "end_time": p.end_time,"duration":int_duration_hours,"star_rating":star_rating,"coach_first_name":coach_first_name,"coach_last_name":coach_last_name,"coach_img":coach_img}
        )
    return session

def get_all_sessions_by_profile(profile: Profile):
    sessions=Training_session.objects.filter(Profile=profile)
    return format_sessions_response(sessions)

def get_sessions_by_date(profile: Profile, date_filter_start: datetime, date_filter_end: datetime):
    conditions = Q(session__id=OuterRef('id')) & Q(date__gte=date_filter_start) & Q(date__lte=date_filter_end)
    sessions = Training_session.objects.filter(Exists(session_date.objects.filter(conditions),Profile=profile))
    return format_sessions_response(sessions)


def get_all_sessions():
    sessions=Training_session.objects.all()
    return format_sessions_response(sessions)


def session_meta_data(session):
            star_rating = get_session_rating(session.id)
            dates = session_date.objects.filter(session=session)             
            first_date=dates.first()
            last_date=dates.last()
            today = date.today()
            print(session)
            start_datetime = datetime.combine(today, session.start_time )
            end_datetime = datetime.combine(today, session.end_time)
            duration = end_datetime - start_datetime 
            duration_hours = duration.total_seconds() / 3600  
            int_duration_hours = int(duration_hours)
            coach_first_name = session.Profile.user.first_name
            coach_last_name = session.Profile.user.last_name
            coach_img = session.Profile.image
            return {
                        "id":session.id,
                        "first_date": first_date,
                        "last_date": last_date,
                        'name':session.name,
                        'small_sum':session.small_sum,
                        'categorie':session.categorie,
                        'img':session.img ,
                        'type':session.type,
                        'price':session.price,
                        'location':session.location.location,
                        'participant_limit':session.participant_limit,
                        "start_time": session.start_time,
                        "end_time": session.end_time,
                        "duration":int_duration_hours,
                        "star_rating":star_rating,
                        "coach_first_name":coach_first_name,
                        "coach_last_name":coach_last_name,
                        "coach_img":coach_img,
                }

def get_all_sessions_by_profile_client(profile: Profile):
    orders = Order.objects.filter(user=profile.user).prefetch_related('ordertoproduct_set')

    ordered_sessions = []

    for order in orders:
        for item in order.ordertoproduct_set.all():
            if item.type == "session":
                    print(item.order_id)
                    session = session_meta_data(item.training_session)
            
                    ordered_sessions.append(
                        {
                          **session,
                          "order_id": item.id
                        }
                    )

    return ordered_sessions



def get_all_sessions_by_profile_client_date(profile: Profile, date_filter_start: datetime, date_filter_end: datetime):
    orders = Order.objects.filter(user=profile.user).prefetch_related('ordertoproduct_set')
    conditions = Q(date__gte=date_filter_start) & Q(date__lte=date_filter_end)
    ordered_sessions = []

    for order in orders:
        for item in order.ordertoproduct_set.all():
            if item.type == "session":
                dates = session_date.objects.filter(conditions, session=item.training_session)
                if dates.count() != 0:
                   session = item.training_session
                   session_meta_data(session)
                   ordered_sessions.append(session_meta_data(session))
                   
    return ordered_sessions

def get_session_rating(session_id):
    reviews=Reviews.objects.filter(session__id=session_id)
    
    stars_count=0
    stars_average=0
    sum_stars=0
    
    if reviews.exists():
        for review in reviews.all():
            sum_stars= review.stars+sum_stars
        stars_count= reviews.count()
        stars_average= sum_stars/stars_count

    return stars_average