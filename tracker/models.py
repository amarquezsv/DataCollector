# tracker/models.py
from django.db import models

class CovidData(models.Model):
    country = models.CharField(max_length=100)
    cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.country} - {self.updated_at}"