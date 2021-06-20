from django.http import response
from django.test import TestCase
from django.urls import reverse
from alimentos.models import Food
import pytest


class TestAlimentos(TestCase):

    def setUp(self):
        food = Food.objects.create(name='Banana', brand='Seu Ze', section='Frutas', content='6', price='2.95' )
        food.save()
        self.response_get = self.client.get('food/')

    # Routes tests
    def test_route_create(self):
        response = self.client.get('/create_food/')
        self.assertEqual(response.status_code, 200)

    def test_route_read(self):
        pass

    def test_route_update(self):
        pass

    def test_route_delete(self):
        pass


