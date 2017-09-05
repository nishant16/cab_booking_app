
from django.conf.urls import url

from companies import views



urlpatterns=[
    url(r'^$', views.login_view, name='login'), #ex:/
    url(r'^signup/', views.signup_view, name='signup'),  # ex:signup/
    # url(r'^post/(?P<id>\d+)/', views.view_post, name='n1'),
    # url(r'^category/(?P<id>\d+)/', views.view_category, name='n2'),
    #

    ]