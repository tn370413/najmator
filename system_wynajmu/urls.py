from django.conf.urls import url
from . import views

urlpatterns = [
    url('user_page', views.user_page, name='user_page'),
    url('estate_page', views.estate_page, name='estate_page'),
    url('estate_edit_page', views.estate_edit_page, name='estate_edit_page')
]
