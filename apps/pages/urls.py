from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path('', views.index,  name='index'),
  path('send-message/', views.send_message_view, name='send_message'),
]
