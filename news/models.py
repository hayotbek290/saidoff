from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _
from .managers import NewsManager



class News(models.Model):
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    is_published = models.BooleanField(_('is published'), default=True)

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title



class NewsImage(models.Model):
    file = models.IntegerField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f"File ID: {self.file}, News Title: {self.news.title}"
