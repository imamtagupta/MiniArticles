from unicodedata import name
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.broadcastingMessage, name='broadcastingMessage'),
    url(r'^bmf/$', views.broadcastingMessageForm, name='broadcastingMessageForm'),

]
