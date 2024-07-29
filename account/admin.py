from django.contrib import admin
from .models import User, UserMessage, Group



admin.site.register(User)
admin.site.register(UserMessage)
admin.site.register(Group)
