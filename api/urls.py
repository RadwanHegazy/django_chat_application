from django.urls import path

from . import views



urlpatterns = [
    path('send_msg/',views.send_msg,name='send_msg'),
    path('get_msgs/',views.all_msgs,name='all_msgs'),
]