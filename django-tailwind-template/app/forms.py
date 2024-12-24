from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exists")
        return username
    

class LoginForm(forms.Form):
    
    username=forms.CharField(required=True)
    password=forms.CharField(required=True)    

class UpdateProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=False,max_length=100)
    last_name=forms.CharField(required=False,max_length=100)
    username=forms.CharField(required=False,max_length=150)
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput,
       
    )
    class Meta:
        model=User
        fields=["first_name","last_name","username","password"]




 