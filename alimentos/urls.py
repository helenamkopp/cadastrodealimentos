from django.urls import path
from alimentos.views import food


urlpatterns = [
    path('food/', food, name='food'),
]
