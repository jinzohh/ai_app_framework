from django.urls import path, re_path
from . import views

app_name = 'demos'

urlpatterns = [

    path('', views.index, name='index'),

    # /chatbot/
    re_path(r'^chatbot/$', views.ChatBot, name='chatbot'),

    # /inputoutput/
    re_path(r'^inputoutput/$', views.InputOutput, name='inputoutput'),
]