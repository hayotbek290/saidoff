from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MediaURLSerializer

# Assuming you have a model named Media with a file field
from .models import Media

class MediaDownloadView(APIView):
    def get(self, request, *args, **kwargs):
        media = Media.objects.all()
        serializer = MediaURLSerializer(media, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
