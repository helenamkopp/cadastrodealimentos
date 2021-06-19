from django.urls import path
from alimentos.views import food, create_food, delete_food, update_food


urlpatterns = [
    path('food/', food, name='food'),
    path('create_food/', create_food, name='create_food'),
    path('update_food/<int:id>', update_food, name="update_food"),
    path('delete_food/<int:id>', delete_food, name="delete_food"),


]
