from django.urls import path
from .views import TestView,ContactWithUsMobileView



urlpatterns = [
    path('test/', TestView.as_view(), name='test_view'),
    path('contact/', ContactWithUsMobileView.as_view(), name='contact_with_us_mobile'),
]
