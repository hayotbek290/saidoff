from django.contrib import admin
from news.models import News, NewsImage
# Register your models here.
@admin.register(News)
class Newsadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']


 
@admin.register(NewsImage)
class NewsImageadmin(admin.ModelAdmin):
    list_display = ['file']