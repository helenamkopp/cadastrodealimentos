from unittest import result
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


    def test_route_read_all(self):
        response = self.client.get('/food/')
        self.assertEqual(response.status_code, 200)


    def test_route_update(self):
        result = Food.objects.last()
        response = self.client.get(f'/update_food/{result.id}')
        self.assertEqual(response.status_code, 200)


    def test_route_delete(self):
        result = Food.objects.last()
        response = self.client.post(f'/delete_food/{result.id}')
        self.assertEqual(response.status_code, 302)

    #Views tests

    def test_template_create(self):
        response = self.client.get('/create_food/')
        self.assertTemplateUsed(response, 'form_food.html')
    
    def test_template_read_all(self):
        response = self.client.get('/food/')
        self.assertTemplateUsed(response, 'food.html')

    # def test_template_update(self):
    #     pass

    # def test_template_delete(self):
    #     pass

