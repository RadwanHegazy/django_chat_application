from django.db import models

# Create your models here.


class User (models.Model) :
    user = models.CharField(max_length=100)

    def __str__(self) :
        return str(self.user)
    
class Room (models.Model) :
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=1000)
    
    def __str__(self) :
        return str(self.name)