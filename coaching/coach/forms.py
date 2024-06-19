from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Training_session


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
        user = super(SignupForm , self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]

        if commit:
            print("user-commit")
            print(user)
            user.save()
        return user
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Training_session        
        fields = ['Profile', 'img']  # Include 'user' field in the form
    
          
class sessionform(forms.ModelForm):
    class Meta:
        model = Training_session        
        fields = ['description', 'name', 'start_time', 'end_time']  # Include 'user' field in the form


    # id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100, null=True)
    # description = models.CharField(max_length=100, null=True)
    # Profile = models.ForeignKey(Profile, on_delete=models.CASCADE) 
    # img = models.ImageField(upload_to="sessions/%y/%m/%d", null=True)
    # start_time = models.DateTimeField(null=True)    
    # end_time = models.DateTimeField(null=True)   
    # location = models.CharField(max_length=100,null=True)
    # participant_limit = models.IntegerField(null=True) 

class FilterForm(forms.Form):
    PRICE_CHOICES = [
        ('under_25', 'Under $25'),
        ('25_to_50', '$25 to $50'),
        ('50_to_100', '50 to $100'),
        ('over_100', 'Over $100'),
    ]
    SORT_CHOICES = [
        ('popularity', 'Popularity'),
        ('high_to_low', 'Price: High to Low'),
        ('low_to_high', 'Price: Low to High'),
    ]
    
    price_range = forms.ChoiceField(
        choices=PRICE_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )