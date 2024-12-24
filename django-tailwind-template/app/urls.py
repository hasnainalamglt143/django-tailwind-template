from django.urls import path
from . import views
from django.contrib.auth.views import (
    
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
 

urlpatterns = [
  
path('',views.home,name="home"),

# authentication urls
    path('register/',views.register,name="register"),
    path('login/',views.Login,name="login"),
    path("logout/",views.Logout,name="logout"),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path("update-profile/",views.updateProfile,name="update-profile")
]


