from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path



urlpatterns = [
    url(r'^accounts/sign_up', views.SignUp.as_view(), name='sign_up'),
    url(r'^pounds/$', views.pound_list, name='pounds'),
    path("fishes/<slug:slug>/", views.fish_details, name='fish_details'),
    url(r'^fishes/$', views.fishes_list, name='fishes'),
    url(r'^pounds/new/$', views.pound_new, name='pound_new'),
    url(r'^review/new/$', views.review_new, name='review_new'),
    # url(r'^reviews/(?P<id>\d+)/', views.review_show, name='review_show'),
    # url(r'^pounds/(?P<id>\d+)/', views.pound_show, name='pound_show'),
    path("pounds/<slug:slug>/", views.pound_show, name='pound_show'),
    path("reviews/<int:id>/", views.review_show, name='review_show'),
    url(r'^$', views.home, name='home'),
    url(r'^test/$', views.bootstrap_test, name='bootstrap_test'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    path("pounds/<slug:slug>/clearphotos/", views.pound_images_clear, name='clear_pound_photos')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
