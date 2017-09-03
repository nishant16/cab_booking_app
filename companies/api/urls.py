
from django.conf.urls import url

# from companies import views
from .views import DriverList
# from .views import CabList



urlpatterns=[
    url(r'^$', DriverList.as_view(), name='index'),
    # url(r'^post/(?P<id>\d+)/', views.view_post, name='n1'),
    # url(r'^category/(?P<id>\d+)/', views.view_category, name='n2'),
    #
    ]