from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login_with_cookie/$', views.login_with_cookie, name='login_with_cookie'),
    url(r'^login_with_session/$', views.login_with_session, name='login_with_session'),
]
