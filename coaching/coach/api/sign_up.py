from django.shortcuts import render, redirect
from coach.forms import SignupForm
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth import login
from coach.models import Profile


def signup(request):
    if request.method == "POST":
        userData = request.POST.copy()
        userData["password1"] = request.POST.get("password")
        userData["password2"] = request.POST.get("password")
        userData["username"] = get_random_string(length=50)

        form = SignupForm(userData)

        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                return render(
                    request,
                    "coach/sign_up.html",
                    {
                        "error_global": "this email is already being used by a different account, try to sign up with a different one",
                    },
                )
            # insert user into database
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            

            return redirect("/")
        else:
            errors = {}
            for field, err in form.errors.items():
                print(f"Field: {field}, Errors: {', '.join(err)}")
                print(", ".join(err))
                errors[field] = ", ".join(err)

            return render(request, "coach/sign_up.html", {"errors": errors})

    else:
        return render(request, "coach/sign_up.html")
