from django.db import models

class Rating(models.Model):
    brewery_name = models.CharField(max_length=100)
    beer_name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=2, decimal_places=1)
    notes = models.TextField(blank=True)
