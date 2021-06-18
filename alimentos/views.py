from django.shortcuts import render, redirect
from .models import Food
from .form import FoodForm

# Create your views here.

def food(request):
    foods = Food.objects.all()
    return render(request, 'food.html', {"foods": foods})

def create_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food')

    return render(request, 'form_food.html', {'form': form})

def update_food(request, id):
    foods = Food.objects.get(id=id)
    form = FoodForm(request.POST or None, instance=foods)
    if form.is_valid():
        form.save()
        return redirect('food')

    return render(request, 'form_food.html', {'form': form})

def delete_food(request, id):
    food = Food.objects.get(id=id)
    food.delete()
    return redirect('food')
