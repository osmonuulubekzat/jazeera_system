from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name="index"),
    path('index', Index, name="index"),
    path('forms', Forms, name="forms"),
    path('message', Message, name="message"),
    path('send-message', SendMessage, name="send-message"),
]
