from django.conf.urls import url
from django.urls import path
from django.conf import settings # necessary?
from django.conf.urls.static import static
from . import views

app_name = 'system'
urlpatterns = [
    url('user_page/', views.user_page, name='user_page'),
    path('estate_page/<int:estate_id>/', views.estate_page, name='estate_page'),
    url('estate_edit_page/', views.estate_edit_page, name='estate_edit_page'),
    path('estate_edit/<int:estate_id>/', views.estate_edit, name='estate_edit'),
    url('estate_add/', views.estate_add, name='estate_add'),
    url('delete_contract/', views.delete_contract, name='delete_contract'),
    path('delete_estate/<int:estate_id>/', views.delete_estate, name='delete_estate'),
    path('photo_upload/<int:estate_id>/', views.photo_form_upload, name='photo_upload'),
    path('photo_list/<int:estate_id>/', views.photo_list, name='photo_list'),
    path('photo_delete/<int:photo_id>/', views.photo_delete, name='photo_delete'),
    path('photo_edit_page/<int:pk>/', views.PhotoEditView.as_view(), name='photo_edit_page'),
    path('photo_upload_edit/<int:pk>/', views.save_from_edit, name='photo_upload_from_edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
