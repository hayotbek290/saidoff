from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'image', _('image') 
        VIDEO = 'video', _('video')
        AUDIO = 'audio', _('audio')
        FILE = 'file', _('file')
        MUSIX = 'music', _('music')


    type = models.CharField(_('type'),max_length=250, choices=MediaType.choices)
    file = models.FileField(_('file'),upload_to='media', validators=[FileExtensionValidator(
        allowed_extensions=['png','jpg','jpeg','gif', 'mp4', 'mp3' ]
    )])


def clean(self):
        # Validate media type
        if self.type not in [self.MediaType.IMAGE, self.MediaType.VIDEO, self.MediaType.AUDIO]:
            raise ValidationError(_("Invalid Media Type"))

        # Validate file name extension based on media type
        ext = self.file.name.split('.')[-1].lower()

        if self.type == self.MediaType.IMAGE:
            if ext not in ['jpg', 'jpeg', 'png']:
                raise ValidationError(_("Invalid Image File"))

        elif self.type == self.MediaType.VIDEO:
            if ext not in ['mp4', 'avi', 'mov']:
                raise ValidationError(_("Invalid Video File"))

        elif self.type == self.MediaType.AUDIO:
            if ext not in ['mp3', 'wav']:
                raise ValidationError(_("Invalid Audio File"))
            
class Meta:
    verbose_name = _('Media')
    verbose_name_plural = _('Media')