from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse

class TestContactWithUsView(APITestCase):

    def setUp(self):
        pass

    def test_happy(self):
        url = reverse('contact_with_us')
        data = {
            "name": "TestName",
            "phone_number": "+998919209292",
            "message": "TestMessage"
        }
        response = self.client.post(url, data, format='json')
        
        
        print(response.content)
        
        
        self.assertEqual(response.status_code, 200) 
        
       
        self.assertEqual(list(response.data.keys()), ['name', 'phone_number', 'message'])
