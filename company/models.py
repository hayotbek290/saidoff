from django.db import models
from common.models import  Media
from django.utils.translation import gettext_lazy as _
from .validators import validate_phone_number,validate_address,validate_location,validate_telegram_url,validate_instagram_url,validate_facebook_url,validate_linkedin_url
# Create your models here.
class Contacts(models.Model):
    adress = models.CharField(max_length=255, validators=[validate_address])
    phone_number = models.CharField(max_length=100, validators=[validate_phone_number])
    email = models.EmailField()
    location = models.URLField(validators=[validate_location])


    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class SocialMedia(models.Model):
    telegram = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()

class ContactWithUsWeb(models.Model):
    name = models.CharField(max_length=255)
    # phone_number = models.CharField(max_length=20) 
    message = models.TextField()

class AppInfo(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

class PrivacyPolicy(models.Model):
    text = models.TextField()

class Sponsor(models.Model):    
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    url = models.URLField()

class ContactWithUsMobile(models.Model):
    email = models.EmailField()
    reason = models.TextField()
    message = models.TextField()
    # file = models.FileField(upload_to='contact_files', null=True, blank=True)

class ContactWithUsCategory(models.Model):
    name = models.CharField(max_length=255)

class ContactWithUsReason(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ContactWithUsCategory, on_delete=models.CASCADE)






##########################################################################

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
