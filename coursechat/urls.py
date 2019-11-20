"""cfehome re_path Configuration

The `re_pathpatterns` list routes re_paths to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/re_paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to re_pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to re_pathpatterns:  path('', Home.as_view(), name='home')
Including another re_pathconf
    1. Import the include() function: from django.re_paths import include, path
    2. Add a re_path to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path ,include
from django.views.generic import TemplateView
# from youtube import urls as youtube_urls
from django.contrib.auth import views as auth_views
import profiles.views as accounts_views


urlpatterns = [
    # path('', TemplateView.as_view(template_name="home.html")),
    path('admin/', admin.site.urls),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='profile/login.html'), name='login'),

    path('chat/', include('chat.urls')),
    path('', include('youtube.urls')),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    # path('hello/', accounts_views.hello, name='home'),

    re_path(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='profile/password_reset.html',
            email_template_name='profile/password_reset_email.html',
            subject_template_name='profile/password_reset_subject.txt'
        ),
        name='password_reset'),
    re_path(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='profile/password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='profile/password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='profile/password_reset_complete.html'),
        name='password_reset_complete'),

    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='profile/password_change.html'),
        name='password_change'),
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='profile/password_change_done.html'),
        name='password_change_done'),
]


