from django.http import JsonResponse
from coach.forms import sessionform
from django.shortcuts import render
from coach.models import Training_session,session_date,session_location
from django.shortcuts import  get_object_or_404
from datetime import datetime
from decimal import Decimal, InvalidOperation
import json 


def update_session(request):
    if request.method != "POST":
        return JsonResponse(            
            {"ok": False, "reason": "redirect", "url": "/shop"}                                                 
        )                                                                                                                           
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')
            categorie = data.get('categorie')
            start_time = data.get('start_time')
            end_time = data.get('end_time')
            categorie_2nd = data.get('categorie_2nd')
            selected_day = data.get('selected_day')
            session_id= data.get('sessionId')
            participent= data.get('max_participent')
            price= data.get('price')
            location = data.get('location')
            # Validate data (simple example, more validation may be needed)
            if not title or not description or not categorie or not start_time or not end_time or not categorie_2nd or not selected_day:
                return JsonResponse({'error': 'Missing data'}, status=400)
            try:
                price = Decimal(price)
            except InvalidOperation:
                return JsonResponse({'error': 'Invalid price format'}, status=400)  
            session = get_object_or_404(Training_session, id=session_id)

            # Create a new instance of MyModel
            session.name = title
            session.description = description
            session.categorie = categorie
            session.type = categorie_2nd
            session.start_time = start_time
            session.end_time = end_time
            session.location = session_location.objects.get(location= location)
            session.price = price
            session.participant_limit = participent
            session.save()
            for date in selected_day:
                session_date.objects.create(session=session , date= datetime.strptime(date, "%Y-%m-%d"))


            return JsonResponse({'status': 'success' ,'data':'session'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
            