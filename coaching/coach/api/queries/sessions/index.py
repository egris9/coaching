from coach.models import Profile,Training_session,session_date
from datetime import datetime, date
from django.db.models import  Exists, Q, OuterRef


def format_sessions_response(sessions):
    session = []
    for p in sessions:
        first_date=session_date.objects.filter(session=p).first()
        last_date=session_date.objects.filter(session=p).last()

        today = date.today()
        start_datetime = datetime.combine(today, p.start_time )
        end_datetime = datetime.combine(today, p.end_time)
        duration = end_datetime - start_datetime 
        duration_hours = duration.total_seconds() / 3600  
        int_duration_hours = int(duration_hours)

        session.append(
            {"id":p.id,"first_date": first_date, "last_date": last_date,'name':p.name,'small_sum':p.small_sum, 'categorie':p.categorie,'img':p.img ,'type':p.type,'price':p.price,'location':p.location.location,'participant_limit':p.participant_limit,"start_time": p.start_time, "end_time": p.end_time,"duration":int_duration_hours}
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