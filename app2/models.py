from django.db import models
from app1.models import UserProfile

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=50,blank=False,null=True)
    no = models.IntegerField()
    userprofile = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.userprofile)

class Test():
    pass

class Abc():
    pass