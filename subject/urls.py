
from django.urls import path
from .views import TestView, ContactWithUsMobileView

urlpatterns = [
    path('test/', TestView.as_view(), name='test-view'),
    path('contact/', ContactWithUsMobileView.as_view(), name='contact-with-us-mobile-view'),
]
urlpatterns = [
    path('contact/', ContactWithUsMobileView.as_view(), name='contact-with-us-mobile-view'),
]
