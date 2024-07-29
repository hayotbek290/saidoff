from django.http import JsonResponse
from django.views.generic import View
from .models import TestModel
from .serializers import TestModelSerializer

class TestView(View):
    def get(self, request):
        test_objects = TestModel.objects.all()
        serializer = TestModelSerializer(test_objects, many=True)
        return JsonResponse(serializer.data, safe=False)
