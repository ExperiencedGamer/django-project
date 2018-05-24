from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\d+)$', views.details, name='details'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/$', views.account_view, name='account'),
    url(r'^account/settings/$', views.accountSettings, name='accountSettings'),
    url(r'^profile/(?P<username>\w+)/$', views.accountUrl, name='accountUrl'),
    url(r'^profile/edit/$', views.editProfile, name='editProfile'),
    url(r'^profile/passreset/$', views.passwordReset, name='passwordReset')
]
