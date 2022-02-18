#(5 points) As a developer, I want to create a GET by id endpoint that does the following things:
#Accepts a value from the request’s URL (the super id) | returns a 200 status code | Responds with the super in the database that has the id that was sent through the URL.
    #line 52 and lines 56-58
#(5 points) As a developer, I want to create a POST endpoint that does the following things:
#Accepts a body object from the request in the form of a Super model | Adds the new super to the database | Returns a 201 status code | Responds with the newly created super object
    #line 26 and lines 46-50
#(5 points) As a developer, I want to create a PUT endpoint that does the following things:
#Accepts a value from the request’s URL (super id) | Finds the super in the Super table and updates that super with the properties that were sent | Returns a 200 status code | Responds with the newly updated super object
    #line 52 and lines 59-63
#(5 points) As a developer, I want to create a DELETE endpoint that does the following things:
# Accepts a value from the request’s URL | Deletes the correct super from the database | Returns a 204 status code (NO CONTENT)
    #line 52 and lines 64-66
#(10 points) As a developer, I want to create a GET endpoint the responds with a 200 success status code and all of the supers within the supers table.
#View function should be implemented in a way to accept a “type” parameter (e.g. http://127.0.0.1:8000/api/supers?type=hero) for "hero" and "villain" | If no type query parameter is sent, return a custom object response with a “heroes” and a "villains" 
    #line 26 and lines 29-45

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from .models import SuperTypes
from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        super_types = SuperTypes.objects.all()
        supertype_param = request.query_params.get('type')  
        if supertype_param:
            supers = Super.objects.all() 
            supers = supers.filter(super_type_id__type=supertype_param)
            serializers = SuperSerializer(supers, many = True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        elif super_types:
            custom_response_dictionary = {}
            for supertype in super_types:
                supers = Super.objects.filter(super_type_id=supertype.id)
                super_serializer = SuperSerializer(supers, many=True)
                custom_response_dictionary[supertype.type] = {
                    "supers": super_serializer.data
                }        
            return Response(custom_response_dictionary, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = SuperSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  
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