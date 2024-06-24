from django.shortcuts import render
from coach.api.top_session import top_sessions

def home(request):
    sessions = top_sessions()
    return render(
        request,
        'coach/home.html',{"sessions":sessions}
    )
