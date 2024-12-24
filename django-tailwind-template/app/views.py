from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import (CustomUserCreationForm,UpdateProfileForm,LoginForm)



def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
      form = CustomUserCreationForm(request.POST)
      if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
         
          return redirect("login")

      else:
       
          return render(request,"users/register.html")

    else:
        return render(request,"users/register.html")




def Login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data["password"]
            username=form.cleaned_data['username']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
             
               return render(request, "users/login.html")
        else:
            return render(request, "users/login.html")

 
    else:
        return render(request,"users/login.html")


def Logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')    



@login_required(login_url='/login/')
def updateProfile(request):
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # Ensure that the password field is not accidentally modified
            user = form.save(commit=False)
            if 'password' in form.cleaned_data:
                # Handle password change properly if it's included in the form
                user.set_password(form.cleaned_data['password'])
            user.save()

            # Refresh the session to prevent logging out after a password change
            
            update_session_auth_hash(request, user)

         
            return redirect("update-profile")  # Redirect to a suitable page
        else:
            form = UpdateProfileForm(instance=request.user)

    return render(request, "users/change-profile.html")



