from django.contrib import admin
from .models import Room, User as us
from django.contrib.auth.models import Group, User


admin.site.register(Room)
admin.site.register(us)
admin.site.unregister(Group)
admin.site.unregister(User)