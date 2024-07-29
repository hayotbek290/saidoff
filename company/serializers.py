from rest_framework import serializers
from .models import FAQ,TestModel



class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'


    
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model =FAQ
        exclude = ("id,")

