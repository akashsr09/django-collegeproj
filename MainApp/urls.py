# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns= [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/reg_done/$', views.reg_done, name='reg_done'),
    url(r'^login/login_done/$', views.login_done, name='login_done'),
    url(r'^sorry/$', views.sorry, name='sorry'),
]

