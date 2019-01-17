from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pound_list, name='pound_list'),
]
