#(2.5 points) As a developer, I want to create a SuperTypes model in a “super_types” app. Property names must be in snake_case and match the following exactly!
# type – CharField

from django.db import models

class SuperTypes(models.Model):
    type = models.CharField(max_length=255)

