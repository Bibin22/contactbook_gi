from django.urls import path
from .views import *

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('contact_add', contact_add, name='contact_add'),
    path('contact_details/<str:pk>', contact_details, name='contact_details'),
    path('contact_delete', contact_delete, name='contact_delete'),
    path('contact_edit/<str:pk>', contact_edit, name='contact_edit')
]