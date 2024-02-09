from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('api/message/', message_create, name='message_create'),
    path('api/create_new_gpt/', create_new_gpt, name='create_new_gpt'),
    path('api/list_custom_gpts/', list_custom_gpts, name='list_custom_gpts'),
    path('api/sendFireData/', sendFireData, name='sendFireData'),
    path('api/getOAI/', getOAI, name='getOAI'),
    path('api/list_feedback_gpts/', list_feedback_gpts, name='list_feedback_gpts'),
    path('api/feedback_message_api/', feedback_message_api, name='feedback_message_api'),
    path('api/feedbackList/', feedbackList, name='feedbackList'),
    path('api/scList/', scList, name='scList')
]