from math import fabs
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        max_length = 30,
        unique = True,
    )
    description = models.CharField(
        max_length = 120,
        unique = False,
    )
    quantity = models.IntegerField(
        unique = False,
        regex = r'^([0-9]|[1-9][0-9]|100)$',
    )
