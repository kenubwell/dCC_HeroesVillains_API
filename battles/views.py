#BONUS - Create CRUD endpoints for the table in the "battle(s)" app

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BattleSerializer
from .models import Battle


@api_view(['GET', 'POST'])
def battles_list(request):

    if request.method == 'GET':
        battles = Battle.objects.all()
        custom_response_dictionary = {}
        count = 1
        for battle in battles:
            battlers = Battle.objects.filter(id=battle.id)
            serializers = BattleSerializer(battlers, many=True) #this is going to take our product table and convert to json
            custom_response_dictionary[battle.id] = {
                f"Battle {count}": serializers.data
            }
            count += 1
        return Response(custom_response_dictionary, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = BattleSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def battles_detail(request, pk): #this pk allows for input for the product id

    battle = get_object_or_404(Battle, pk=pk)  #since I imported django shortcut (above) we can use this function to check for errors. Just have to enter (Model, Value)
    if request.method == 'GET':
        serializer = BattleSerializer(battle)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    elif request.method == 'PUT':
        serializer = BattleSerializer(battle, data=request.data) #this compares current product data and takes in requested data from user
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        battle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)