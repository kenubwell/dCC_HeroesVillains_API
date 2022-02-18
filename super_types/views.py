from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupertypeSerializer
from .models import SuperTypes


@api_view(['GET', 'POST'])
def supertypes_list(request):

    if request.method == 'GET':
        stypes = SuperTypes.objects.all()
        serializers = SupertypeSerializer(stypes, many=True) #this is going to take our product table and convert to json
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = SupertypeSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supertypes_detail(request, pk): #this pk allows for input for the product id

    stype = get_object_or_404(SuperTypes, pk=pk)  #since I imported django shortcut (above) we can use this function to check for errors. Just have to enter (Model, Value)
    if request.method == 'GET':
        serializer = SupertypeSerializer(stype)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    elif request.method == 'PUT':
        serializer = SupertypeSerializer(stype, data=request.data) #this compares current product data and takes in requested data from user
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        stype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)