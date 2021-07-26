from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=False)
    address = models.CharField(blank=False,null=True,max_length=255)
    birth_date = models.DateTimeField(blank=True)
    changed_on = models.DateTimeField(blank=False,auto_now=True)
    created_on = models.DateTimeField(blank=False,auto_now_add=True)


    def __str__(self):
        return self.user.username 