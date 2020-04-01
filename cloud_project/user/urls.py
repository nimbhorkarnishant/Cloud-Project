from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from user import views as user_views


urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home1,name='home1'),
    path('signup/',views.register_user,name='register'),
    path('login/',views.login,name='login'),
    path('login_validition/',views.login_validition,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('otp_validiation/',views.otp_verification,name='otp_form'),
    path('View_profile/',views.view_profile_data,name='View_profile'),
    path('edit_profile/',views.edit_profile_data,name='edit_profile'),
    path('updating_profile_detail/',views.update_user_detail,name='updating_profile_detail'),
    #path('set_password/',views.set_user_password,name='set_password'),





]
