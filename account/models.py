from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
##############################################################EMAILVALIDATOR
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Group(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class UserMessage(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    message = models.TextField(_('message'))
    file = models.ForeignKey(Media,on_delete=models.SET_NULL,null=True,blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)