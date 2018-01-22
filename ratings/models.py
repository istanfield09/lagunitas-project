from django.db import models

class Rating(models.Model):
    brewery_name = models.TextField(default="No brewery")
    beer_name = models.TextField()
    score = models.DecimalField(max_digits=2, decimal_places=1)
    notes = models.TextField(blank=True)
