from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('chat/submit/', views.chat_submit, name='chat_submit'),
]