from rest_framework import serializers
from .models import Battle

class BattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = ['id', 'battle_date', 'super_one', 'super_two', 'super_one_id', 'super_two_id']
        depth = 1
    
    super_one_id = serializers.IntegerField(write_only = True)
    super_two_id = serializers.IntegerField(write_only = True)