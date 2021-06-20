from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    content = models.FloatField()
    price = models.FloatField()

    def price_food(self):
        return f"The {self.name} cost {self.price}"

    def __str__(self) -> str:
        return f"{self.name} - {self.brand} - {self.section} - {self.content} - {self.price}"
