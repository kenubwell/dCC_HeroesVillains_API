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
        custom_response_dictionary = {}
        for supertype in super_types:
            supers = Super.objects.filter(super_type_id=supertype.id)
            super_serializer = SuperSerializer(supers, many=True)
            custom_response_dictionary[supertype.type] = {
                "supers": super_serializer.data
            }        
        return Response(custom_response_dictionary)
    elif request.method == 'POST':
        serializers = SuperSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)  #this validates that API user input is true or accurate to the database
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def supertypes_list(request):

#     supertype_param = request.query_params.get('type')
#     supers = Super.objects.all()
#     if supertype_param:
#         supers = supers.filter(super_type_id__type=supertype_param)
#         serializers = SuperSerializer(supers, many = True)
#     return Response(serializers.data, status=status.HTTP_200_OK)


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