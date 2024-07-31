from django.http import JsonResponse
from django.views.generic import View
from .models import TestModel
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  ContactWithUsMobileSerializer
from django.http import HttpResponse

class TestView(View):
    def get(self, request):
        return HttpResponse('This is the TestView')

class ContactWithUsMobileView(APIView):
    def post(self, request):
        serializer = ContactWithUsMobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
