from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pounds/$', views.pound_list, name='pounds'),
    url(r'^$', views.home, name='home'),
]
