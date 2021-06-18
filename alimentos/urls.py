from django.urls import path
from alimentos.views import food, create_food, delete_food


urlpatterns = [
    path('food/', food, name='food'),
    path('create_food/', create_food, name='create_food'),
    path('delete_food/<int:id>', delete_food, name="delete_food"),

]
