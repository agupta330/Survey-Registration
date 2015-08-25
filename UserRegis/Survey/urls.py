__author__ = 'sbodduluri2'
from django.conf.urls import patterns, url
from Survey import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^check/$', views.some_view, name=''),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),# ADD NEW PATTERN!
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^survey1/$', views.survey1, name='survey1'),
    url(r'^Profile/$', views.edit_profile, name='Profile'),
    url(r'^update/$', views.update, name='update'),
    )