#BONUS - You will need to create a "battle" app and a Battle model. The Battle model will be a junction table and have the following properties:
# super_one - ForeignKey (to super table) | super_two - ForeignKey (to super table) | battle_date - DateTimeField

from django.db import models
from super_types.models import SuperTypes
from supers.models import Super

class Battle(models.Model):
    super_one = models.ForeignKey(Super, on_delete=models.CASCADE, related_name='super_one')
    super_two = models.ForeignKey(Super, on_delete=models.CASCADE, related_name='super_two')
    battle_date = models.DateTimeField()