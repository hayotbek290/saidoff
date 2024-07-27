from rest_framework import serializers

class MediaURLSerializer(serializers.Serializer):
    def to_representation(self, obj):
        try:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.file.url)
        except Exception as e:
            return None
