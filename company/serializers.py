from rest_framework import serializers
from .models import ContactWithUs,FAQ


class ContactWithUsSesializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = ("name","phone_number","massage")
         
    def create(self, validated_data):
        return ContactWithUs.objects.create(**validated_data)
    
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model =FAQ
        exclude = ("id,")

