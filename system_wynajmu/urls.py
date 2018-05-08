from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'system'
urlpatterns = [
    url('user_page/', views.user_page, name='user_page'),
    path('estate_page/<int:estate_id>/', views.estate_page, name='estate_page'),
    url('estate_edit_page/', views.estate_edit_page, name='estate_edit_page'),
    url('estate_edit/', views.estate_edit, name='estate_edit'),
    url('estate_add/', views.estate_add, name='estate_add'),
    url('delete_contract/', views.delete_contract, name='delete_contract'),
    url('delete_estate/', views.delete_estate, name='delete_estate')
]
