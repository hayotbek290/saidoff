from django.db import models
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
    telegram =  models.URLField(validators=[validate_telegram_url])
    facebook =  models.URLField(validators=[validate_facebook_url])
    instagram =  models.URLField(validators=[validate_instagram_url])
    lenkedin =  models.URLField(validators=[validate_linkedin_url])


    def __str__(self):
        return self.title


class ContactWithUs(models.Model):
     name = models.CharField(max_length=100)
     phone_number = models.CharField(max_length=100, validators=[validate_phone_number])
     massage = models.TextField()

     class Meta:
         verbose_name = _('Contact With Us')
         verbose_name_plural = _('Contacts')
     def __str__(self):
         return self.name


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()  

    class Meta:
        verbose_name = "FAQ"