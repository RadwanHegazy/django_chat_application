from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('room/<int:roomid>/',views.room,name='room'),
    path('logout/',views.logout,name='logout'),
]