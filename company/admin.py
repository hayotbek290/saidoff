from django.contrib import admin
from .models import (
    Contacts, SocialMedia, ContactWithUsWeb, AppInfo, FAQ,
    PrivacyPolicy, Sponsor, ContactWithUsMobile,
    ContactWithUsCategory, ContactWithUsReason
)
# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id","phone_number"]
    list_editable = ["phone_number"]
    
    
@admin.register(SocialMedia)
class SoocialAdmin(admin.ModelAdmin):
    list_display = ["id", "telegram"]
    list_display_links = ["telegram"]



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["id","question","answer"]





#############################################################################################


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ["id", "text"]

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ["id", "image", "url"]

@admin.register(ContactWithUsMobile)
class ContactWithUsMobileAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "reason", "message"]

@admin.register(ContactWithUsCategory)
class ContactWithUsCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(ContactWithUsReason)
class ContactWithUsReasonAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category"]
