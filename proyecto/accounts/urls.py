from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.register, name='signup'),
    path('profile/', views.profile, name='profile'),

    path('password/', PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url='/accounts/password/done/'
    ), name='password_change'),

    path('password/done/', PasswordChangeDoneView.as_view(
        template_name='accounts/password_done.html'
    ), name='password_done'),
]