from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('api/message/', message_create, name='message_create'),
    path('api/create_new_gpt/', create_new_gpt, name='create_new_gpt'),
    path('api/list_custom_gpts/', list_custom_gpts, name='list_custom_gpts'),
]