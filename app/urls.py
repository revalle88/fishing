from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pounds/$', views.pound_list, name='pounds'),
    url(r'^pound/new/$', views.pound_new, name='pound_new'),
    url(r'^$', views.home, name='home'),
]
