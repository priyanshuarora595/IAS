from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.login_req,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_req,name='logout'),
    
    # path('change_user_password', views.change_user_password,name='change_user_password'),
        
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="reset/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="reset/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset/password_reset_done.html"), 
        name="password_reset_complete"),
]
