from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    content = models.FloatField()
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.name} - {self.brand} - {self.section} - {self.content} - {self.price}"
