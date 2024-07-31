from django.shortcuts import render
from django.views import View




class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'template_name.html')

class ContactWithUsMobileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'template_name.html')