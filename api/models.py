from django.db import models
from frontend.models import User, Room

# Create your models here.



class Message (models.Model) :
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.CharField(max_length=1000,null=True,blank=True)
    img = models.FileField(upload_to='images/',max_length=1000,blank=True,null=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        if self.body :
            return str(self.body)
        else:
            return str(self.img.url)  