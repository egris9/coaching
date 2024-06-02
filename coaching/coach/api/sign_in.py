from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from coach.forms import SigninForm 
from django.contrib.auth.models import User


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email)
                if username is not None:
                    user = authenticate(request, username=username, password=password)
                    print(f"Email: {email}, Password: {password}, user:{user}")

                    if user is not None:
                       login(request, user)
                       return redirect('/')
            except User.DoesNotExist:
                return render(request, 'coach/sign_in.html', {'error_message': "this user does not exist"})
            
        error_message = 'Invalid login credentials. Please try again.'
        return render(request, 'coach/sign_in.html', {'error_message': error_message})
        
  
    else:
        return render(request, 'coach/sign_in.html')