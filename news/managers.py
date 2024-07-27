from django.db import models

class NewsManager(models.Manager):
    def create_news(self, title, description, image=None):
        news = self.create(title=title, description=description, image=image)
        return news
