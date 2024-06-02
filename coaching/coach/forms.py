from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SigninForm(forms.Form):
        email = forms.EmailField(required=True)
        password = forms.CharField(max_length=50)  
        

class SignupForm(UserCreationForm):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]

        if commit:
            print("user-commit")
            print(user)
            user.save()
        return user
