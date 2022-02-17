from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        supers = Super.objects.all()
        serializers = SuperSerializer(supers, many=True) #this is going to take our car table and convert to json
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = SuperSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk): #this pk allows for input

    super = get_object_or_404(Super, pk=pk)  #since imported django shortcut we can use this function to check for errors. Just have to enter (Model, Value)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)  
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)