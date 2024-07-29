from rest_framework import serializers
from .models import FAQ,TestModel,ContactWithUsMobile



class ContactWithUsMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUsMobile
        fields = ['email', 'reason', 'message', 'file']


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'


    
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model =FAQ
        exclude = ("id,")

