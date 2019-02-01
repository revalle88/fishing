from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pounds/$', views.pound_list, name='pounds'),
    url(r'^pound/new/$', views.pound_new, name='pound_new'),
    url(r'^review/new/$', views.review_new, name='review_new'),
    url(r'^reviews/(?P<id>\d+)/', views.review_show, name='review_show'),
    # url(r'^reviews/<int:id>/', views.review_show, name='review_show'),
    url(r'^$', views.home, name='home'),
]
