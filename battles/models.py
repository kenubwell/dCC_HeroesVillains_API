from django.db import models
from super_types.models import SuperTypes
from supers.models import Super

class Battle(models.Model):
    super_one = models.ForeignKey(Super, on_delete=models.CASCADE, related_name='super_one')
    super_two = models.ForeignKey(Super, on_delete=models.CASCADE, related_name='super_two')
    battle_date = models.DateTimeField()