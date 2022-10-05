from django.db import models

# Create your models here.
class Thing():
    name = models.CharField()
    description: models.TextField()
    quantity = models.IntegerField()
