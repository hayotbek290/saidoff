# company/validators.py

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(phone_number):
    phone_regex = re.compile(r'^\+998\d{9}$')
    if not phone_regex.match(phone_number):
        raise ValidationError(_("Phone number must be in the format: '+998XXXXXXXXX' where X is a digit."))

def validate_address(address):
    if len(address) < 10:
        raise ValidationError(_("Address must be at least 10 characters long."))

def validate_location(url):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if not url_regex.match(url):
        raise ValidationError(_("Invalid URL format."))
def validate_telegram_url(value):
    regex = re.compile(r'^https:\/\/t\.me\/[a-zA-Z0-9_]+$')
    if not regex.match(value):
        raise ValidationError(_('Invalid Telegram URL.'))

def validate_instagram_url(value):
    regex = re.compile(r'^https:\/\/www\.instagram\.com\/[a-zA-Z0-9_.]+\/?$')
    if not regex.match(value):
        raise ValidationError(_('Invalid Instagram URL.'))

def validate_linkedin_url(value):
    regex = re.compile(r'^https:\/\/www\.linkedin\.com\/in\/[a-zA-Z0-9-]+\/?$')
    if not regex.match(value):
        raise ValidationError(_('Invalid LinkedIn URL.'))

def validate_facebook_url(value):
    regex = re.compile(r'^https:\/\/www\.facebook\.com\/[a-zA-Z0-9.]+\/?$')
    if not regex.match(value):
        raise ValidationError(_('Invalid Facebook URL.'))


# company/models.py

