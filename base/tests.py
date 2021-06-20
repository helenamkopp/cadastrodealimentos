from django.http import response
from django.test import TestCase
from django.urls import reverse
import pytest

HOME = 'home'


class TestBase(TestCase):
    

    def test_route_base_home_return_status_code_200(self):
        response = self.client.get(reverse(HOME))
        self.assertEqual(response.status_code, 200)
    
    def test_route_use_template(self):
        response = self.client.get(reverse(HOME))
        self.assertTemplateUsed(response, 'home.html')